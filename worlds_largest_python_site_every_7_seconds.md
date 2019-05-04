World's Largest Python Site every 7 minutes
Instagram - 
Releases 70-100 times daily - average every 7 minutes
(How many people are in instagram's eng team)

Evolution:
1. Deploy script that copies to host, unpacks, change symlink after monitoring canary, release for each host]
(Probably scp)
Deploy script has a lock to prevent multiple users from deploying at once
Anyone can deploy code
Scaled to small # of engineers

Issues: (RE humans)
immediate deploys are not guaranteed
Inconsistent human response to options in deploy script
"Tests failed. Still deploy? (Y/N)"

Do not present options to do so (automatically)


2. Deploy automation pipeline with autodefaults
No human input when deploying
Still used deploy script under the covers
Now get CD!

CD as a service
- fewer people understand deployment process and how to revert
- job of deployment team to unblock things when the build fails

Not scalable because of deployment team

3. Idea: Don't break trunk - don't land broken code
Before merging, paralellize deployment pipeline and test against branch that has had master rebased plus using canary

Positive:
Each commit is gtg before allowing to land
- Commit author owns change
- Fewer instances of broken trunk/master
- everyone 

Commit will be pushed to prod within 1 hour of commit landing
Hot fixes are fast - there is no difference between that and "regular deploys"

Postmordems when things break
Why did tests/canary did not catch this

4. Deploy in phases
Add an additional tiers - c1 2% of all hosts, c2 everything

Adds time onto deployment process up to 10 minutes
(Do c1 env use different %2?)
Everything is pipelined

Now everything is too complicated, so we throw away deployment script

Built a controller to control whether things are being deployed to c1, c2
runners manage actual deployments
Db stores contents of c1, c2 environments, data is pushed by commit process
( go back and look at slides for this)

Commit takes even longer to get to production because of time in c1, c2


5. Deploy as fast as possible
Why?
Engineers are around ti fix
Engineers don't have to slow down
Better productivity/safety

Arrange the ability to deploy multiple commits at a time so that commits don't take more than 1 hour
However, we can only deploy at the speed of capacity loss budget

Built a hot swap system in uWSGI using idle uWSGI worker
(Go back and look at presentation)

6. Fully autonomous fleet
Used to be 100% homogeneous
Now allowed to differ
Eventually did a 2-to-3 migration
C1, c2 stages permanent
Segments of containers/machines running different versions of software

Eventually refactored Deploy in Phases run system to remove runners and now compute units read config data from caches


( go back and look at presentation)

Major concepts: 
Do the simple things first- Do not try hopping from beginning to end
Deploy as fast as possible
Build a culture around testing
