Building a culture of observability

== What is Rover? "AirBnB for dogs"

== What is observability at Rover? Why is it important?
Encompasses monitoring in a big way
Observability is:
- Knowing what's going on inside of the web app
- When things go wrong, what happened?

== Goals:
Tell the narrative of the application
Empower developers


Complexity of Rover's web app
600, 000 lines of python code in a Django monolith
Celery tasks, etc
100 developers
15-30 deploys a day

What does this (observability) give us?
The ability to wrangle a complex web app
- much faster bug resolution
- significantly reduced time to identify production issues
- more thorough root cause analysis


== How do we do it with web apps?

The pillars of observability
- Useful Logs
- Granular Metrics
- Narrative-driven dashboards

== Logging:

"Writing things down as they happen"
General best practices
Log to stderr/stdout, then aggregate somewhere searchable like ELK stack, loggly, sumo logic
Logs can come from everywhere, like system processes, nginx, etc

It becomes difficult to see one workflow (async, web requests, proxy jumps, etc) as scale increases
You can't depend on timestamps (prone to clock drift)

=== Unifying logs
Generating tracing ids and injecting into logs - That way you can get all events associated with a particular workflow
Implementation: use thread local storage, then inject these into each log record with a logging.Filter

Complexity: managing thread local storage (but it's nbd in Django, flask with middleware)

This isn't the complete story:
1. It can be too granular
2. It's hard to monitor
3. Expensive: cost is ~ linear with growth

== Metrics:

Big 3:
- Error rate
- Response time
- volume/throughput

Not enough for Rover. They also needed query logging everywhere - probably necessary for naive use of ORMs
- number of queries per type
- amount of time spent performing queries
- per request for each view
- per execution per Celery tasks

Useful tech: Statsd, Datadog, (others)

Implementation: wrap database queries with metrics
Pretty easy with Django 2.0+ - `connection.execute_wrapper` - otherwise maybe have to create a custom database backend
Do not emit a counter per query - aggregate these until the end of the task or request and emit a histogram

== Dashboards: How to visualize this data in a useful way

Make it easy:
- visual diffs
- trends

Make the dashboards self-documenting if possible - put what it is in the title

Examples:
Medium query count per request (as histogram) to detect n+1 queries
Median query time per request per view to detect queries that grow linearly with table size (missing index?)
Slow queries from $database by view to determine where the expensive queries are (could use some tuning via indices, etc)

Putting it all together!

Building observability culture
- create, document, and share tools (evangelism)
- Do not make observability opt-in
- Measure everything - err on the side of too granular



