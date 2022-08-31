---
keywords: fastai
description: Statistics is the study of how to collect, analyze, and draw conclusions from data. It’s a hugely valuable tool that you can use to bring the future into focus and infer the answer to tons of questions. Updating ...
title: Introduction to Statistics in Python
toc: true
branch: master
badges: true
comments: true
author: Datacamp
categories: [Python, Data Visualization, EDA, Time Series, Machine Learning, scikit-learn, Regression, classification, Tempogram, Spectrogram, Cross-valiation, Stationarity]
image: images/stats_intro.png
hide: false
search_exclude: true
metadata_key1: metadata_value1
metadata_key2: metadata_value2
nb_path: _notebooks/Introduction to Statistics in Python/2022-08-31-Introduction to Statistics in Python.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/Introduction to Statistics in Python/2022-08-31-Introduction to Statistics in Python.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<blockquote><p>Statistics is the study of how to collect, analyze, and draw conclusions from data. It’s a hugely valuable tool that you can use to bring the future into focus and infer the answer to tons of questions. For example, what is the likelihood of someone purchasing your product, how many calls will your support team receive, and how many jeans sizes should you manufacture to fit 95% of the population? In this course, you'll discover how to answer questions like these as you grow your statistical skills and learn how to calculate averages, use scatterplots to show the relationship between numeric values, and calculate correlation. You'll also tackle probability, the backbone of statistical reasoning, and learn how to use Python to conduct a well-designed study to draw your own conclusions from data.</p>
</blockquote>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">warnings</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">rcParams</span><span class="p">[</span><span class="s1">&#39;figure.figsize&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="mi">8</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>

<span class="n">pd</span><span class="o">.</span><span class="n">set_option</span><span class="p">(</span><span class="s1">&#39;display.expand_frame_repr&#39;</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">DeprecationWarning</span><span class="p">)</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">FutureWarning</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Summary-Statistics">Summary Statistics<a class="anchor-link" href="#Summary-Statistics"> </a></h2><blockquote><p>Summary statistics gives you the tools you need to boil down massive datasets to reveal the highlights. In this chapter, you'll explore summary statistics including mean, median, and standard deviation, and learn how to accurately interpret them. You'll also develop your critical thinking skills, allowing you to choose the best summary statistics for your data.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="What-is-statistics?">What is statistics?<a class="anchor-link" href="#What-is-statistics?"> </a></h3><blockquote><p><strong>Descriptive and inferential statistics</strong>
<strong>Data type classification</strong></p>
</blockquote>
<h3 id="Measures-of-center">Measures of center<a class="anchor-link" href="#Measures-of-center"> </a></h3><blockquote><p><strong>Mean and median</strong>
<strong>Mean vs. median</strong></p>
</blockquote>
<h3 id="Measures-of-spread">Measures of spread<a class="anchor-link" href="#Measures-of-spread"> </a></h3><blockquote><p><strong>Quartiles, quantiles, and quintiles</strong>
<strong>Variance and standard deviation</strong>
<strong>Finding outliers using IQR</strong></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Random-Numbers-and-Probability">Random Numbers and Probability<a class="anchor-link" href="#Random-Numbers-and-Probability"> </a></h2><blockquote><p>In this chapter, you'll learn how to generate random samples and measure chance using probability. You'll work with real-world sales data to calculate the probability of a salesperson being successful. Finally, you’ll use the binomial distribution to model events with binary outcomes.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="What-are-the-chances?">What are the chances?<a class="anchor-link" href="#What-are-the-chances?"> </a></h3><blockquote><p><strong>With or without replacement?</strong>
<strong>Calculating probabilities</strong>
<strong>Sampling deals</strong></p>
</blockquote>
<h3 id="Discrete-distributions">Discrete distributions<a class="anchor-link" href="#Discrete-distributions"> </a></h3><blockquote><p><strong>Creating a probability distribution</strong>
<strong>Identifying distributions</strong>
<strong>Expected value vs. sample mean</strong></p>
</blockquote>
<h3 id="Continuous-distributions">Continuous distributions<a class="anchor-link" href="#Continuous-distributions"> </a></h3><blockquote><p><strong>Which distribution?</strong>
<strong>Data back-ups</strong>
<strong>Simulating wait times</strong></p>
</blockquote>
<h3 id="The-binomial-distribution">The binomial distribution<a class="anchor-link" href="#The-binomial-distribution"> </a></h3><blockquote><p><strong>Simulating sales deals</strong>
<strong>Calculating binomial probabilities</strong>
<strong>How many sales will be won?</strong></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="More-Distributions-and-the-Central-Limit-Theorem">More Distributions and the Central Limit Theorem<a class="anchor-link" href="#More-Distributions-and-the-Central-Limit-Theorem"> </a></h2><blockquote><p>It’s time to explore one of the most important probability distributions in statistics, normal distribution. You’ll create histograms to plot normal distributions and gain an understanding of the central limit theorem, before expanding your knowledge of statistical functions by adding the Poisson, exponential, and t-distributions to your repertoire.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="The-normal-distribution">The normal distribution<a class="anchor-link" href="#The-normal-distribution"> </a></h3><blockquote><p><strong>Distribution of Amir's sales</strong>
<strong>Probabilities from the normal distribution</strong>
<strong>Simulating sales under new market conditions</strong>
<strong>Which market is better?</strong></p>
</blockquote>
<h3 id="The-central-limit-theorem">The central limit theorem<a class="anchor-link" href="#The-central-limit-theorem"> </a></h3><blockquote><p><strong>Visualizing sampling distributions</strong>
<strong>The CLT in action</strong>
<strong>The mean of means</strong></p>
</blockquote>
<h3 id="The-Poisson-distribution">The Poisson distribution<a class="anchor-link" href="#The-Poisson-distribution"> </a></h3><blockquote><p><strong>Identifying lambda</strong>
<strong>Tracking lead responses</strong></p>
</blockquote>
<h3 id="More-probability-distributions">More probability distributions<a class="anchor-link" href="#More-probability-distributions"> </a></h3><blockquote><p><strong>Distribution dragging and dropping</strong>
<strong>Modeling time between leads</strong>
<strong>The t-distribution</strong></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Correlation-and-Experimental-Design">Correlation and Experimental Design<a class="anchor-link" href="#Correlation-and-Experimental-Design"> </a></h2><blockquote><p>In this chapter, you'll learn how to quantify the strength of a linear relationship between two variables, and explore how confounding variables can affect the relationship between two other variables. You'll also see how a study’s design can influence its results, change how the data should be analyzed, and potentially affect the reliability of your conclusions.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Correlation">Correlation<a class="anchor-link" href="#Correlation"> </a></h3><blockquote><p><strong>Guess the correlation</strong>
<strong>Relationships between variables</strong></p>
</blockquote>
<h3 id="Correlation-caveats">Correlation caveats<a class="anchor-link" href="#Correlation-caveats"> </a></h3><blockquote><p><strong>What can't correlation measure?</strong>
<strong>Transforming variables</strong>
<strong>Does sugar improve happiness?</strong>
<strong>Confounders</strong></p>
</blockquote>
<h3 id="Design-of-experiments">Design of experiments<a class="anchor-link" href="#Design-of-experiments"> </a></h3><blockquote><p><strong>Study types</strong>
<strong>Longitudinal vs. cross-sectional studies</strong></p>
</blockquote>
<h3 id="Congratulations!">Congratulations!<a class="anchor-link" href="#Congratulations!"> </a></h3>
</div>
</div>
</div>
</div>
 
