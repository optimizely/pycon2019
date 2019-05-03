# Mocking and Patching Pitfalls

Speaker: Edwin Jung, Staff Software Engineer, data engineering and microservices at Quid (make sense of large amounts of unstructured text)

> History, opinions, speculation, biased talk, about how I have used mock and use mock.

Intermediate to advanced talk. Should have used mocking or patching before. Maybe you use mock and patch APIs regularly but are not sure why they are sometimes painful.

Things you might learn, styles of unit test, where mocks came from, alternatives to mocking, antipatterns in mocking, relationships

Also see "Demystifying the Patch Function" - PyCon Cleveland 2018


## Nine Circles of Mock Hell

See photo on Trent's camera


8. Using the debugger to reverse-engineer mocks
9. So much mocking that I don't even want to rewrite the code 


## The Promise (what mock promises)

1. Mock - library to isolate code for testing
2. How to use Mock, MagicMock, patch, spec, autospec, side_effect, etc.
3. Patching is tricky - target the right namespace
4. By the way, be careful about overmoocking!

- see: typical example of mock in slides
- real example - guardian feed: English news site with REST API for search
    - find all relevant articles with "brexit" over a time period and feed URLs to a scraper


## Deep mocking can become really confusing

- How many mocks are you really creating?
  - How much of that is just implementation detail?
  - How much is necessary information that the test needs to know about?
  - "law of demeter" violation
    - chaining method calls into an object's instance variables
  - tests trivially breakable, what if we change imports in a harmless way? e.g. `import redis` to `from redis import Redis`


> Maybe you need to look into why there is so much heavy mocking

> Patching is a sign of failure, the more you have to patch the more you have failed - Michael Ford


## Mocks In Context

- see photo in my camera (or slides)


## Contrary Opiniona

- Always use mocks as a last resort. Mocks create trouble in tests, "Unit Testing" book with samurai on cover.
- Unit Testing book - _


## How to test without mocks?

- Mocks aren't stubs, mocks != stubs, stubs are not mocks

### Test Doubles

- A thing you can sub for the real thing in your test. A mock is just one kind of double.

- 5 definitions of test doubles (see slides
  1.
  2. 
  3. 
  4. 
  4. 

#### Stub

Canned value that is used later.

Alternative: Fake patching, define fake function. use patch(thing to patch, new=fake_function)

#### Dependency Injection

Alternative: Fake Injection - decouple module from specific db implementation


### Tactical Questions

1. Which test doubles (mock or other)?
2. Mockist or Classical style testing? (aka London or Detroit?)
3. Patch or inject test double before testing it?


## Lets review the guardian feed test...

See map in slides

What are the roles in the guardian collaboration? Source, Parser, Sink.

1. Find a seam
2. Patch a fake

> A seam is a place where you can alter behavior without editing in that place.

Seams: tcp, urllib3, requests internals. Easiest probably request with `HTTMock` library

### HTTMock

- use httmock.urlmatch to redirect traffic from a url to a function
- use httmock.HTTMock for _

### Inject the redis connection

- `fakeredis` library - make a fake connection, lpop data off.
- inject the collaborator, some function that acts like a datastore


## Last tactic - go functional

> The real problem is that your functions have side effects. Pure functions == No Problems


## Antipatterns

- bootleg TDD: aim for 100% isolation, 100% coverage...
- procedural decomposition: break down problems into smaller subproblems, recursive repeat
  - then you test p, mock a, e, test e, should you mock the db connection, mock the query language?
    - Tests fail because SQL whitespace changed... wtf
    - mocking is supposed to be an exploratory design tool
- patching creates an obstacle to understanding dependency inversion  
  - dependency inversion: no dependencies from core code to outside, core code does not care about outside, if its a webapp or gui
    - ports-and-adapters, clean architecture, hexagonal, etc., onion architecture
- "the blob" - one massive codebase with no tests and few outputs
  - favorite of data scientists
  - too late to unit test, patch tactically...
  - what kind of test is this? integration?
- patches as crosscuts
  1. a test should test a single behavior
  2. a patch is a violation of some encapsulation boundary
  3. a test with many patches is violating multiple encapsulation boundaries

  - _ ? (see slides)
  - a test case with many cases represent a cross-cutting concern


## Opinions

- always be refactoring
- consider other test doubles
- patching
  - should be rare, the last tool you use
- mocks (if you decide to use them)
  - should target ??? ... see slides

## Books

Python Testing with Pytst - Briank Okken
___


## Other Resources

See slides

