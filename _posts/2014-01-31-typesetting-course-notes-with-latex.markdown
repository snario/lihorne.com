---
layout: post
title: "Typesetting with LaTeX"
date: 2014-01-31 23:22:09 -0800
comments: true
categories: typesetting
---

<!--* list element with functor item
//{:toc}-->

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


## Introduction

One of the first courses that a student in the Mathematics faculty at the University of Waterloo takes is MATH 135 / 145 (Algebra), a course in learning how to write concise mathematical proofs. The professor that directed this course decided in my year of taking it to provide `.tex` templates for students to use to typeset their assignments. I had never heard of or seen anyone use LaTeX before but thought I'd take a shot at it so I didn't have to write anything down for my first year Calculus and Algebra weekly assignments.

First,  what is LaTeX? Essentially, LaTeX is to a book what a set of blueprints is to a building. It doesn't have to be a book though, it can be an academic paper, an article, a homework assignment, or really any document at all. In the sense that you produce documents using LaTeX, it is a lot like Microsoft Word. A major difference however is that with Word, what you see is what you get, meaning that you are editing a document that looks exactly like what you would print. With LaTeX, you use a markup language to precisely format your document and write the content, and then run a program on what you've written which will output a typeset document.

For the most part, LaTeX is used in scientific publications, and very often in mathematics papers; it is most popular in academia. The reason it is so useful for mathematicians and scientists is because dealing with mathematical notation is much easier than dealing with some equation editor. Additionally, LaTeX is a massive project and comes with many libraries and packages that can be used with make references, bibliographies, tables of content, sections, tables, figures, etc much easier to format and automate.

For example if I were to write using LaTeX:

{% highlight latex linenos %}
This is Euler's equation: $e^{i\pi} + 1 = 0$
{% endhighlight %}

it would be typeset to become:

$$\mbox{This is Euler's equation: } e^{i\pi} + 1 = 0$$

This can get really messy really quickly, but once you learn the basics of the language and use it frequently, it becomes much faster than writing or using an equation editor. For example, Schrödinger's equation:

{% highlight latex linenos %}
-\frac{\hbar}{2m}\f{\di^2 \Psi(x,t)}{\di x^2}+U(x)\Psi(x,t)=i\hbar\frac{\di\Psi(x,t)}{\di t}
{% endhighlight %}

$$- \frac{\hbar}{2m} \frac{\partial^2 \Psi(x,t)}{\partial x^2} + U(x)\Psi(x,t) = i \hbar \frac{\partial \Psi(x,t)}{\partial t}$$

If you're interested in learning the language and getting started using LaTeX, my advice would just be to force yourself to do an assignment using it or otherwise to write a report or paper with it. The best way to learn how to use it is to just dive right in and try your best to figure things out as you go. A quick way to do this would be to check out [writeLaTeX](https://www.writelatex.com), an online tool for writing LaTeX. If you're interested in an in-depth beginner's guide, try using [this one from Princeton University](https://www.cs.princeton.edu/courses/archive/spr10/cos433/Latex/latex-guide.pdf).


##  Workflow

Since typesetting my assignments for that Algebra course in my first term, I began writing my assignments for all of my other courses in LaTeX as well, and then in Fall 2013 decided to try to typeset not just all of my assignments, but all of my course notes too. Since LaTeX is so versatile, I was able to take notes of equations in calculus, graphs in combinatorics, and code in a few computer science courses. If you're interested in these notes or in an example of what a typeset document looks like, they're posted on this website [right here](https://lihorne.com/course-notes).

To begin, I use the [MacTex distribution](https://tug.org/mactex/) (it really is 2.3GB, LaTeX is huge) on my computer. The way I manage to take notes is by using [Sublime Text](https://www.sublimetext.com/) with the PDF reader [Skim](https://skim-app.sourceforge.net/). There is a package for Sublime text called [LaTeXTools](https://github.com/SublimeText/LaTeXTools) which makes this setup really quick and easy. To install LaTeXTools you will need [Package Control](https://sublime.wbond.net/) for Sublime as well.

Once everything is in order, you should be able to hit ⌘-B within Sublime Text on a `.tex` file and have it compile your code to PDF. Now, this post is meant to be about how to quickly take course notes using LaTex, so I'll go through a few methods I used to do that this semester and really quickly. First though, I'd like to mention that the main inspiration my course notes are the notes that [Michael Baker has on his website ](https://triple-involution.blogspot.ca/p/notes.html), for any pure mathematics students at the University of Waterloo, they are perfect.


##  Template

When I started taking course notes, I knew that it would take a lot of time to deal with little templating issues such as dealing with sections and revisions, links to pages, definitions, theorems, counters, code, etc that would be a waste of time during class to fix. So, I made [this course notes template](https://www.github.com/snario/notes-template) which asks for only a little information and then lets you write away to actually copy down notes. For example,

{% highlight latex linenos %}
\newcommand{\thiscoursecode}{MATH 136}
\newcommand{\thiscoursename}{Linear Algebra}
\newcommand{\thisprof}{Prof. Dan Wolczuk}
\newcommand{\me}{Liam Horne}
\newcommand{\thisterm}{Winter 2013}
\newcommand{\website}{LIHORNE.COM}
{% endhighlight %}

produces this:

<div class="post-image">
    <img src="https://i.imgur.com/D6zKY1x.png" alt="notes"/>
</div>

Hopefully this will be useful if you're trying to save time and get started right away. There are also many benefits of using this template, for example you can quickly make definitions or theorems from some settings in `notes.sty`, for example

{% highlight latex linenos %}
\begin{defn}[graph]\label{graph}
A \textbf{graph} $G$ is a finite set $V(G)$ of elements called \textbf{vertices},
together with a set $E(G)$ of unordered pairs of distinct vertices.
\end{defn}
{% endhighlight %}

The argument inside the square brackets will be the official name of whatever you're defining, and the `\label{graph}` part defines a quick and unique label for you to use as reference later in the document. For example, if I want to reference back (create a link to) the definition of a graph, then I would write `\nameref{graph}` and a link would be typeset.


###  Code

When it comes to typesetting code, the best package to use is called [Listings](ftp://ftp.tex.ac.uk/tex-archive/macros/latex/contrib/listings/listings.pdf), which offers all sort of customization for ways to display code. To start, define your favourite style with `lstset`, you can customize the language it recognizes, any borderes, line numbers, styles for different types of code, background colours and much more.

{% highlight latex linenos %}
\lstset{
    language=c++,
    basicstyle=\ttfamily\small,
    breaklines=true,
    prebreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\hookleftarrow}},
    frame=none,
    showtabs=false,
    showspaces=false,
    showstringspaces=false,
    morecomment=[l][\color{magenta}]{\#},
    keywordstyle=\color{blue}\bfseries,
    stringstyle=\color{green!50!black},
    commentstyle=\color{gray}\itshape,
    numbers=left,
    captionpos=t,
    backgroundcolor=\color{white},
    escapeinside={\%*}{*)}
}
{% endhighlight %}

Then, inside your main document, write code inside a `lstlistings` block:

{% highlight latex linenos %}
\begin{lstlisting}[language=lisp]
    (define sum (lambda args (foldr + 0 args)))
\end{lstlisting}
{% endhighlight %}

You can also specify a different setting for something you set earlier if you want a one-time code block setting. The package handles syntax colouring by having a list of keywords saved for the many languages it supports, you can also add additional keywords if you'd like.

###  Graph Theory

Trying to draw graphs in real time during class is definitely the most irritating part about using LaTeX, as there is no way of getting around the fact that it will just always be quicker to draw it by hand. If you'd still like to typeset them however, the best way to do it I found is to use [TikZ](https://cremeronline.com/LaTeX/minimaltikz.pdf). Essentially, you will have to define nodes on a 2D plane, then define connections between nodes. The best way to do this quickly is to define a macro within Sublime Text, something short like `grph` that when typed expands out to a skeleton for the graph. Without writing a cleaner solution, this is the quickest I could do it in class. An example of the Petersen graph:

{% highlight latex linenos %}
\begin{center}
    \begin{tikzpicture}
    [scale =.8, auto=left, every node/.style={circle, fill=blue!20}]
    \node (a) at (0,1) {};
    \node (b) at (1,0)  {};
    \node (e) at (-1,0)  {};
    \node (d) at (-0.5,-1) {};
    \node (c) at (0.5,-1)  {};
    \node (A) at (0,2) {};
    \node (B) at (2,0)  {};
    \node (E) at (-2,0)  {};
    \node (D) at (-1.5,-2) {};
    \node (C) at (1.5,-2)  {};

    \foreach \from/\to in {A/B,B/C,C/D,D/E,A/a,B/b,C/c,D/d,E/e,a/c,b/e,c/e,d/a,E/A,d/b}
      \draw (\from) -- (\to);
    \end{tikzpicture}
\end{center}
{% endhighlight %}
Which produces a graph looking like:

<div class="post-image">
    <img src="https://i.imgur.com/pRrXGGE.png" alt="petersen"/>
</div>

You have the option of giving a node a label which would appear inside the circle, in this case the nodes don't have any. There are also a few special cases, for example with matchings or covers. You may want to specify a specific set of nodes to be coloured differently or a set of edges to be drawn with thick lines. These should be farely quick and easy with this method, for example a matching could be drawn with a second `\foreach` loop and the set of edges that are matching, then a `[line width=1mm]` tag.

###  Natural Deduction

If you ever take a course in logic, you will encounter natural deduction. One of the most common notations for natural deduction is called 'flag-notation' and the best way to mimic that notation in LaTeX is to use a package called [Flagderiv](https://svn.win.tue.nl/trac/fmlatex/wiki/Package/Flagderiv). The syntax looks a little like this:

{% highlight latex linenos %}
\begin{flagderiv*}
    \step{pre}{(p \lor q) \ar r}{Premise}
    \assume{p}{p}{Assumption}
      \step{porq}{(p \lor q)}{$(\lor +)$ on \ref{p}}
      \step{r}{r}{$(\ar -)$ with \ref{porq} and \ref{pre}}
    \conclude{}{(p \ar r)}{}
\end{flagderiv*}
{% endhighlight %}

Which produces a proof that looks like:

<div class="post-image">
    <img src="https://i.imgur.com/4zYNXnL.png" alt="nd"/>
</div>


###  Other Things

There are a lot of little things in LaTeX that might take some time when you're typesetting a report or course notes, and there's no way to cover all of them but here are a few that might be helpful:

* Substacks

{% highlight latex linenos %}
\lim_{\substack{\Delta x \rightarrow 0 \\ \Delta y \rightarrow 0}} \sum_{i =1}^n f(x_1,y_i) \Delta x_i \Delta y_i
{% endhighlight %}

$$\lim_{\substack{\Delta x \rightarrow 0 \\ \Delta y \rightarrow 0}} \sum_{i =1}^n f(x_1,y_i) \Delta x_i \Delta y_i$$

* Matrices

{% highlight latex linenos %}
DF(x_1, \ldots, x_n) = \mtx{D_1F_1 & D_2F_1 & \cdots & D_nF_1 \\
                            D_1F_2 & D_2F_2 &  \cdots & D_nF_2 \\
                            \vdots & \vdots & \ddots & \vdots \\
                            D_1F_n & D_2F_n & \cdots & D_nF_n}
{% endhighlight %}

$$DF(x_1, \ldots, x_n) = \begin{bmatrix}D_1F_1 \quad D_2F_1 \quad \cdots \quad D_nF_1 \\ D_1F_2 \quad D_2F_2 \quad  \cdots \quad D_nF_2 \\ \vdots \quad \vdots \quad \ddots \quad \vdots \\ D_1F_n \quad D_2F_n \quad \cdots \quad D_nF_n\end{bmatrix}$$

* Fancy Tables

{% highlight latex linenos %}
\begin{tabular}{c | c | c }
  Name & $\vdash$ Notation & Inference Notation \\
  \hline
  \hline
  \ &&\\
  $\forall$-elimination ($\forall -$) & If $\Sigma \vdash \forall x. \varphi$
  then $\Sigma \vdash \phi[x/t]$ & $\displaystyle{\f{\forall x. \phi}{\varphi[x/t]}}$ \\[3ex]
  \hline
  \hline
  \ &&\\
  $\forall$-introduction ($\forall +$) & If $\Sigma \vdash \varphi[x/u]$
  then $\Sigma\vdash\forall x.\varphi$ & $\displaystyle\f{\varphi[x/u]}{\forall x.\varphi}$\\[3ex]
  \hline
  \hline
\end{tabular}
{% endhighlight %}

<div class="post-image">
    <img src="https://i.imgur.com/oRmKvZU.png" alt="borzoo"/>
</div>

Okay, so I've tried to list as many helpful tools and resources for taking course notes using LaTeX that I've found or used in my experience with it, and I hope that these will be useful for anybody interested in trying out LaTeX in the future for their assignments, course notes, or any other document. It is a very powerful tool that can probably be used in every situation that you've encountered in school before where you had to write an essay, a paper, report, or even a presentation. Once you get the hang of it, you'll be able to make these sorts of documents much faster and much easier than before. For now, see [my course notes](https://www.lihorne.com/course-notes) if you're interested.
