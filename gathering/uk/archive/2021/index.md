---
layout: gathering
title: MathsJam Gathering 2021
---

This is a list of talks given at the 2021 MathsJam Gathering, along with a brief description, and links to slides or other relevant content where we have them. If you spot any mistakes on this page, or would like to update the description of your talk, use the 'Edit this page' link at the bottom with a GitHub account to propose changes and make a pull request.

Andrew Taylor has produced a [poster of the things that happened at MathsJam 2021](https://www.andrewt.net/img/mathsjam-notes/2021.png). There is also a [Cake page here]({{site.url}}/gathering/uk/archive/2021/cakes) with the photos of cakes entered in the cake competition.

The gathering took place on 20th - 21st November 2021.

## Saturday

### SESSION 1

#### Phil Ramsden  - Thought You Were Clever When You Lit The Fuse
You have an unlimited collection of fuses, each of which burns for one hour if lit at one end, and half an hour if lit at both ends at once. Using two fuses, can you time 3/4 of an hour? Using as many fuses as you like, can you time 5/4 of an hour? 

The exact origin of this popular type of puzzle is hard to trace, but it was described as "old" in 1999. Here we're interested in the general question: what durations can we time with our fuses, and what can't be timed in this way? 

Let's call a number "fusible" if there exists a fuse-burning algorithm that will time that exact duration in hours. It's really not hard to show that all non-negative integers are fusible, and that every fusible number is a rational whose denominator is a power of 2, but that not all such rationals are fusible. 

With a bit more sweat, we can also show that the fusible numbers accumulate on the positive integers from the left: that is, for positive integer n, there's no greatest fusible number less than n.

However, they don't accumulate from the right. For example, there's a *least* fusible number *greater* than 1, namely 9/8. And there's a least fusible number greater than 2, namely 513/256. In fact, CLAIM: given any positive integer n, there exists a least fusible number greater than n.

This claim is *true*. What's more, this claim is also *proved*. However, it can't be proved using the common-or-garden axioms of arithmetic; we need *transfinite induction* to do the job.

So here we have a statement that can be stated using the language of arithmetic, and that's true, but that can't be *proved* using the axioms of arithmetic. That makes this claim about fuses, which originated in recreational maths puzzles, a natural Gödel sentence for the Peano axioms. I love that.

#### Ben Sparks  - The Cake and the Candles

A puzzle with multiple solution methods, and musings arising.

#### Sam Hartburn  - Extreme String Art (Without the String)

You can make lovely string art by using straight lines to join equally-spaced points on a circle. But why stick to a circle? By changing the initial curve (and using a lot of lines) you can generate a plethora of beautiful designs.

- [Sam's Geogebra applet](https://www.geogebra.org/m/waej2e7y)

#### Laurence O'Toole  - Predicting Groupthink 2 - A Magic Trick

If everybody in a group has a completely free choice of number, is the result always the same?

### SESSION 2

#### Alexander Bolton  - The Longest Chess Game?

The World Chess Federation has some rules to prevent games from going on forever. I will outline a proposal by Tom Murphy VII for the longest possible legal chess game, and show the Twitter bot that I made to celebrate this achievement.

- [Alexander's slides (PDF)]({{site.url}}/assets/talks/2021/AlexanderBolton-TheLongestChessGame.pdf)

#### Philipp Reinhard  - Disturbing Mandelbrot

We'll explore what happens if we play around with the definition of the Mandelbrot set. There will be lots of pictures and animations. And the Riemann zeta function will make an appearance. 

- [Philipp's slides (PDF)]({{site.url}}/assets/talks/2021/PhilippReinhard-DisturbingMandelbrot.pdf)
- [Philipp's slides (PPTX)]({{site.url}}/assets/talks/2021/PhilippReinhard-DisturbingMandelbrot.pptx)

#### Sophie Maclean  - MathsJam and Mental Health (CW: Mental Illness, Hospitals) 

This will be different to most talks in that it will contain no Maths. Instead I want to take this opportunity to start a conversation about mental health in Maths and thank the many members of the MathsJam community who helped me in my recovery from mental illness. In particular Katie Steckles who enabled me to take part in 24 Hour Maths Magic show from an eating disorder ward; Colin Wright who rearranged the BigMathsJam 2020 timetable to match my hospital time table; the Chalkdust team for their unending support and allowing me to be feel myself and normal; and Tom Crawford for supporting me through the podcast I created whilst ill!

- [Edited version of Sophie's slides (PDF)]({{site.url}}/assets/talks/2021/SophieMaclean-MathsJamandMentalHealth.pdf)


#### Cesco Reale  - Online World Championship of Abstract Games for Nations

I will present the Mochalunt, Online World Championship of Abstract Games for Nations, that will start probably in January: definition of abstract games, spirit and structure of the tournament, questions.

#### Gavan Fantom  - Fast Inverse Square Root

The Fast Inverse Square Root is a notorious algorithm for quickly approximating the reciprocal of a square root which is both simple and impenetrable in equal measure. Find out what it is, why it exists, and develop a mathematical intuition for why the f(...) it works.

- [Gavan's slides (PDF)]({{site.url}}/assets/talks/2021/GavanFantom-FastInverseSquareRoot.pdf)

#### Johnny Ball  - How to draw a Perfect Egg Shape using a Pentagon and Pentagram.

Geometry is a magical science that is somewhat neglected in Secondary School Maths these days, in favour of numeracy and statistics. But if we can kindle a feeling for the wonder of Geometry in young people, we could show them how Maths and Nature have so many connections, how Geometry and beautiful design go hand in hand, and how they can turn their maths world into beautiful pictures and wondrous designs.

We have here a Pentagon with a Pentagram inside it. The Pentagram was the Symbol or badge of the Pythagorean's. It is fascinating because longer and shorter lines are always in Golden Ratio to each other. By adding just three lines to the diagram, you have all you need, with a pair of compasses, to draw a perfect Egg. With compasses, form four curves and the Perfect Egg is achieved. Test it by holding a hens egg against it and see how the curves match. So the bottom wider end of a Hen's Egg is an almost perfect semi or half sphere. Now, when a hen lays an egg, which end appears first? It is this wide semi spherical end. Ouch.

### SESSION 3

#### Katie Steckles  - A Fun Integer Sequence 

A famous integer sequence in recreational maths starts 1, 11, 21, 1211, 111221, ... Katie talked about this sequence, which is called the Look and Say Sequence, and posed a few puzzles, such as:
- What's the highest digit you'll find in the sequence as defined, and why?
- What happens if tou use a different starting number?
- What's the most boring number you can start with?

She also explored some variants on the sequence, and explained why she was recently inspired to talk about it.

- [Katie's slides (photo)]({{site.url}}/assets/talks/2021/KatieSteckles-AFunIntegerSequence.pdf)
- [The tweet that inspired the talk](https://twitter.com/aap03102/status/1455052185889292289)
- [A005150, on OEIS](https://oeis.org/A005150)
- [Article Katie wrote about it for Spektrum Scilogs](https://scilogs.spektrum.de/hlf/a-puzzle-for-november/)
- [Original issue of 'Eureka' containing Conway's article](https://www.archim.org.uk/eureka/archive/Eureka-46.pdf)
- [Back issues of Eureka](https://www.archim.org.uk/eureka/archive/index.html)

#### Goran Newsum  - Quadrilateral is a misnomer

Why do most shape names follow a pattern apart but four and three sided shapes don't?

#### Nancy Blachman  - COVID Misinformation Spreads because Many Don’t Understand Maths

Until recently, the general public could get by without understanding probability and statistics. But that changed with COVID-19. Now hundreds of thousands of people haven’t gotten vaccinated and are dying because they don’t understand what they hear or read and social media spreads misinformation rapidly.

- [Nancy's slides (PDF)]({{site.url}}/assets/talks/2021/NancyBlachman-COVIDMisinformationSpreadsbecauseManyDontUnderstandMaths.pdf)
- [Nancy's slides (Google Slides)](https://docs.google.com/presentation/d/1fqW6Wwa3qlUmtvAPZca79xcj7Muy8z9xHHY9-XJ5iQs/edit#slide=id.g1025ff567f7_0_0)

#### Alexandre Muñiz  - Shaker Dice and Edge Labelings

Shaker dice have a channel where balls fall, and numbers on the channel can be read off to determine the result. Finding useful numberings takes us into graph edge labeling.

#### Simon Bexfield - 3D printed objects

A demonstration of some 3D printed mathematical shapes, including a Menger sponge and dissections of polyhedra.

#### Richard Boland  - Generalized Pentagonal Number Theorem

Richard was unable to deliver his talk due to connection issues, but the blurb and slides are below.

A generalization of Euler's pentagonal number theorem defines a modular structure over partitions which extends naturally to overpartitions and higher order 'more-overpartitions' functions for which a combinatorial explanation is an open problem.  A triangle for partitions/overpartitions isomorphic to Pascal's triangle is presented and for which sums of coefficients on lines of a given slope provide a one-to-one correspondence between the mod-restricted partitions and mod-restricted Fibonacci numbers. 

- [Richard's slides (PDF)]({{site.url}}/assets/talks/2021/RichardBoland-GeneralizedPentagonalNumberTheorem.pdf)

## SUNDAY

### SESSION 4

#### Christian Lawson-Perfect  - Each Edge Peach Pear Plum

I've made another baby, so it's time for another talk about baby maths. Each Peach Pear Plum is a classic picture book for babies, with a beautifully simple rhyming scheme. But I've always wished it was more complete. Join me for an Eulerian tour through fantasy land! 

- [Christian's slides (online)](https://somethingorotherwhatever.com/each-edge-peach-pear-plum-mathsjam-2021/)

#### Belgin Seymenoglu  - Zoombinis

Belgin plays the remake of a 90s game that teaches mathematical thinking without any equations.

- [Belgin's slides (PDF)]({{site.url}}/assets/talks/2021/BelginSeymenoglu-Zoombinis.pdf)

#### James Arthur  - Running Around in Circles

Every week I run an event called parkrun, we go around and around in circles and everytime somebody shouts out how many laps we have done. Any loop can have a similar mapping to numbers. Let's explore this briefly.

James used some ideas from Algebraic Topology and more specifically Homotopies to think about in actuality running around in circles is just doing sums.

#### Matt Peperell  - A set of strange notation systems for sequences of permutations

A certain subset of people, who may or may not be mathematicians, care about permutations and sequences thereof. How can we describe these, and how can we easily commit them to memory?

Though musical in nature, church-bell ringing in the UK does not use the standard Western music notation. Instead the music is described as a sequence of permutations and there are a family of related notation systems to describe these sequences.

#### Adam Atkinson  - Is (one of the) biggest always best?

My victims in Pisa (students at open days) often make life needlessly hard for themselves. Multiple times, they have decided that a straightforwardish problem is actually an unsolved problem from a Richard Guy book.

- [Adam's slides (PDF)]({{site.url}}/assets/talks/2021/AdamAtkinson-Is(oneofthe)biggestalwaysbest.pdf)
- [A053020, on OEIS](http://oeis.org/A053020)

#### Daniel Santos  - The Sun Numerical System

This talk is going to introduce you to some concepts of numerical systems and Daniel is going to talk about how some of the features of the Decimal system give confusion and misunderstandings and complexity in Daniel's point of view. A new numerical system without these problems is going to be explained and introduced by the name of Sun Numerical System (or Neonal).

- [Daniel's slides (PDF)]({{site.url}}/assets/talks/2021/DanielSantos-TheSunNumericalSystem.pdf)

### SESSION 5

#### Alison Kiddle  - On Half-Lives and Happiness

This talk is all about half-lives and how they can affect your mood. 

#### Francis Hunt  - Flexagons for Year 8

My employer has just started running some maths clubs for year 8 students. So this talk will just tell or remind you what trihexaflexagons and hexaflexagons are and how to make them, and note the 3 most common problems school students encounter when making them; also you're welcome to the slides and templates (pdf/LaTeX) I used.

- [Francis's slides (PDF)]({{site.url}}/assets/talks/2021/FrancisHunt-FlexagonsforYear8.pdf)

#### Tony Mann  - The "Sleeping Beauty" Paradox

I'll outline the "Sleeping Beauty" problem (which has led to over 100 articles in philosophical journals).

- [Tony's slides (PDF)]({{site.url}}/assets/talks/2021/TonyMann-TheSleepingBeautyParadox.pdf)
- [Tony's slides (PPT)]({{site.url}}/assets/talks/2021/TonyMann-TheSleepingBeautyParadox.pptx)

#### Alistair Bird  - The Princess is in another Castle

My quixotic quest to search for the seemingly shifting origins and variants of the “Princess in a Castle” logic problem.

Tracking down the origins of a puzzle is as futile as looking for the origins of a joke. But I tried for this apparently recent puzzle. We also look at variants and what makes a good one.

#### Colin Wright  - Coincidences and Lovely Things in Maths

A short time ago on Twitter there was a thread of coincidences in maths, which evolved into a collection of generally lovely things.  Here are some of them.

- [The tweet that inspired the talk](https://twitter.com/kyledevans/status/1454348348669022209)
- [Colin's Chart of tweets](https://www.solipsys.co.uk/Chartter/1454348348669022209.svg)
