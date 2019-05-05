# Strategies for testing Async code

Speaker : Neil Chazin

All code posted in a GH repo: https://bit.ly/nchazin-pycon2019

**NOTE**: These notes don't really give much more context than the link above. :-(

## Asyc Concepts

Coroutines: Perform async work
    - An interface that allows you cooperative concurrency while I/O is handled

Event Loop: Runs coroutines and schedules I/O work to resume coro execution.

Syntax:

    async def my_coro():
        return await another_coro()


`async` : Define a coroutine
`await` : Call a coroutine

When you invoke a coroutine, you get an object that represents eventual completion.
You wait for this object to complete using `await`.

## Testing coroutines can feel like herding cats

Example code "Cat" class: pet method, async move method.

Petting cat makes it pleased. Move will make cat move eventually if pleased.

Test case:

    async def herd(cat, direction):
        cat.pet()
        return await cat.move(direction)

    class Test(unittest.TestCase):

        def test_herd(self):
            garfield = cat.Cat('Garfield')
            # Looked like this first:
            # result = herd(garfield, 'forward')

            # But that never awaits the coro, so await it:
            result = await herd(garfield, 'forward')
            assert result


Problems:
1. Test case looks straight-foward, but it's actually broken because of an un-awaited coro.
2. Need to call coros from inside other coros. Need an event loop to start an initial coro.

Framework support:
- pytest-asyncio

`asyncio.run` makes stuff easier (i.e. call coro without an explicitly defined loop or plugin support):


    class Test(unittest.TestCase):

        def test_herd(self):
            garfield = cat.Cat('Garfield')
            # Use asyncio.run to await teh coro
            result = asyncio.run(herd(garfield, 'forward'))
            assert result


## Next challenge is mocks/patches

If we `@mock.patch` `cat.Cat.move` and accept a mock, things get funky.

Mocks can't be used in an await expression.

Luckily can use an "AsyncMock":

    class AsyncMock(MagicMock):
        async def __call__(self, *args, **kwargs):
            return super().__call__(*args, **kwargs)


Usage: `@patch('cat.Cat.move', new_callable=AsyncMock)`

## Context Managers

Similar to mock:

    class AsynContextManager(mock.MagicMock):
        async def __aenter__(self, *args, **kwargs):
            return super().__enter__(*args, **kwargs)

        async def __aexit__(self, *args, **kwargs):
            return super().__exit__(*args, **kwargs)


## Other challenges/patterns

Some coros don't run in the main thread when executing-- see "Loop Runner" code for a solution.

Hard to test sync functions that call into event loops.

Functional tests (e.g. accepting network I/O) are hard(er).

Event Loop variants (e.g. UVLoop) can have subtle differences. Didn't talk too much about this. :-(

"Loop Runner" : subclasses threading.Thread and runs the coro in the same thread as the event loop.

"Herder" : Look for this in deck.
