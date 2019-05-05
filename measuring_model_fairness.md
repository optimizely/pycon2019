Measuring Model Fairness

It's pretty commonly expected that ML models have a big effect on peoples' lives.
Advertising models affect what sort of things you see.
ML models can even determine how long you spend in jail.

It's important to be sure that the results of these ML models are fair.
Fairness is not well defined, though.

Mentioned Compass Recidivism Model
This model determines whether a person convicted a crime will go on commit another crime
Pro-publica did some stories about this
What they found was that the ML model's error rates were different for different races.
False positive rates for black and white are 44.9% and 23.5%, respectively!
False negative rates for black and white are 28% and 47.7%, respectively!

Pro-publica: "This model is biased against black criminals".
Compass put out a rebuttal citing the overall accuracy is very similar for black and white recipients.

Is this model fair? Who is right?
It is not mathematically possible to balance false positive/negative rates and overall accuracy.

How do we decide what is an appropriate way to decide what makes things fair?


Subtleties:
1. Different groups can have different ground truth positive rates.
For example: Breast cancer in men and women. For women, it's 12% and for men, it's 0.1%
Certain fairness methods make assumptions about the balances of these ground proofs.

Method
Disparate impact: The probability of a positive classification ation between two different groups
This needs to be close to 1, but it is not possible here.

2. We don't know what the ground truth is? We only know what the data says, which is a biased representation of ground truth.
All datasets are biased, some datasets are useful.

A protected attribute can effect how individuals are assigned different labels.

Equal Opportunity - comparing the true positive rate between two different truths. Given in the dataset, you are labeled as 1, what is the probability that you will be marked as a 1.

Sample biases - different groups are sampled into your dataset in different ways
People of AA and Latino decscent are stopped more often than white people after controlling for other factors. The sampling bias is different for different groups.

This is a problem for measuring fairness because some metrics look at classification ratios between groups.

3. The consequences of your model matter.
If the consequences of your model are punitive, you may be more concerned about false positives.
If the consequences of the model are positive, you may be more concerned about false negatives.

Main point of this talk:
You can't math your way out of having to think about fairness. A human still needs to think about ethical considerations of your model.

When ML started to be applied to different domain, people thought of it as just math. Now, that's sort of debunked, but there's a temptation to take that same reasoning and apply it further down the modeling chain: I will add this constraint to my math and it will be fair. A person must be involved.

This is all pretty theoretical so far.

(Real life hypothetical model was detailed here, but it was too fast to get down)
We examined raw dataset and then injected various type of bias into the dataset.
When ground truth is totally balanced, things look pretty good. Disparate impact is close to 1.
Things are messed up when ground truth is imbalanced. 
Label bias is very hard to detect.

You have to think hard about these bias gotchas when you go to determine these fairness metrics

Tools:
Equitas - a python library and web frontend, you provide some data, then select the protected group, then select the fairness metric, then the tool will tell you how those metrics evaluate on your dataset
Pros: easy to use
Cons: nonstandard academic license

IBM AI 360 Open Source Toolkit
Lots of good stuff
Pros: comprehensive!
Cons: probably more comprehensive than you need, lots of reps

Things to be used to determine why model is making a particular conclusion
Lime, shap

THINK ABOUT PROBLEM YOU ARE TRYING TO MODEL, THINK ABOUT POSSIBLE SAMPLE BIASES

USE A DIVERSE TEAM TO CREATE THESE MODELS - SAME SOCIAL CONTEXT, ETC WILL HAVE BLIND SPOTS

KNOW ABOUT YOUR DATA, THINK ABOUT THE CONSEQUENCES


