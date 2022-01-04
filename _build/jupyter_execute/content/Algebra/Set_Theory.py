#!/usr/bin/env python
# coding: utf-8

# # Set Theory
# 
# ## Definition of sets
# 
# ### Sets and their elements
# Basic notion in set theory is a <span style='color:blue'>*set*</span>. A set is a collections of <span style='color:blue'>*elements*</span>. We say that *$a$ is an element of set $A$* or *$a$ is not an element of set $A$*, and we write it as $a\in A$ and $a\not\in A$, respectively. A given set can be for example described by listing all its elements, in this case we use the curly brackets to write $A=\{a,b,c,d\}$. Alternatively, we can define sets by specifying the properties of its elements, for example $B=\{x:x\mbox{ is an even number}\}$. There are some commonly used sets for which we use specific symbols, for example:
# - $\mathbb{N}=\{1,2,\ldots\}$ - the set of all natural numbers 
# - $\mathbb{Z}=\{\ldots,-2,-1,0,1,2,\ldots\}$ - the set of all integers
# - $\mathbb{Q}=\{\frac{p}{q}:p,q\in\mathbb{Z} \wedge q\neq 0\}$ - the set of all fractions
# - $\mathbb{R}$ - the set of all real numbers
# - $\mathbb{C}$ - the set of all complex numbers
# 
# Two sets $A$ and $B$ are <span style='color:blue'>*equal*</span> if and only if they have the same elements, i.e.
# 
# $$
# \boxed{A=B\Leftrightarrow \forall_{x} \,(x\in A\Leftrightarrow x\in B)}
# $$
# 
# > The sets $\{2,5,9,3,5\}$ and $\{3,9,5,2\}$ are equal.
# 
# ### Subsets
# 
# If $A$ and $B$ are sets and
# 
# $$
# \boxed{\forall_x \,(x\in A\Rightarrow x\in B)}
# $$
# 
# then $A$ is called a <span style='color:blue'>*subset*</span> of $B$ and denote it by $A\subseteq B$. In other words, $A$ is a subset of $B$ if all elements of set $A$ are also elements of set $B$. It is always true that $A\subseteq A$. In the case when $A\subseteq B$ and there exist element of set $B$ that are not elements of set $A$, then we call set $A$ a proper subset of $B$ and denote it by $A\subset B$. 
# 
# ***Add picture of a subset***
# 
# > Let $A=\{2,4,6,8\}$ and $B=\{1,2,3,4,5,6,7,8,9,10\}$. Then $A\subset B$.
# 
# ### Empty set
# 
# The set that does not contain any elements is called the <span style='color:blue'>*empty set*</span> and it is usually denoted by $\emptyset$.
# > The set $\{x\in \mathbb{R}:x^2=-1\}$ is empty since there is no real number that when squared gives $-1$.
# 
# > The empty set is a subset of any other set. In other words, for any set $A$, we can write $\emptyset \in A$.
# 
# ### Equal sets
# 
# Two sets are equal if the first one is a subset of the second one and vice versa:
# 
# $$
# \boxed{A=B\Leftrightarrow (A\subseteq B\wedge B\subseteq A)}
# $$
# 
# ### Power set
# 
# The set containing as elements all subsets of a given set $A$ is called the <span style='color:blue'>*power set*</span> of $A$ and is denoted by $\mathcal{P}(A)$, i.e $\mathcal{P}(A)=\{B:B\subseteq A\}$.
# > The power set of $A=\{a,1,\square\}$ is
# >
# >$$
# \mathcal{P}(A)=\{\emptyset,\{a\},\{1\},\{\square\},\{a,1\},\{a,\square\},\{1,\square\},\{1,a,\square\}\}
# $$
# 
# - If the set $A$ has $n$ elements, then its power set $\mathcal{P}(A)$ has $2^n$ elements.
# - For any set $A$ it is always true that $\emptyset\in \mathcal{P}(A)$.
# 
# ### Cardinality
# 
# The number of elements of a finite set $A$ (a set with finite number of elements) is called its <span style='color:blue'>*cardinality*</span>, and is denoted by $|A|$. 

# In[27]:


from jupytercards import display_flashcards

display_flashcards('https://raw.githubusercontent.com/tomaszlukowski/Compendium-of-University-Mathematics/main/json/first.json')


# In[ ]:




