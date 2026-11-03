1,Introduction
	(background, historical text, multiple versions, examples)
  * Many historical narratives were copied, adapted and retold over several centuries, 
  	and consequently survive in multiple versions.
  * Well-known examples include the Middle English Canterbury Tales (), 
  	the Middle High German Nibelungenlied (Batts, 1971) and the Irish Acallam na Senórach (Cnockaert-Guillou, 2025).

  (requirements, comparison is important in textual scholarship)
  * Comparison is one of the fundamental activities of humanities scholarship (Unsworth, 2000), 
  	and it becomes central when a text survives in multiple versions (Haentjens Dekker et al., 2015).
  * Philologists, as well as other scholars and learners who engage with such texts, need to identify similarities and differences 	   between versions: how names and words are spelled (Bollmann, 2019), how writing conventions change, 
  	how the plot diverges, where a passage appears in each version, 
  	and how text lost through damage in one version might be recovered from another.

  (manually and is time- cosuming, resource-heavy and error-prone, Computational support therefore has the potential)
  * When preparing critical editions, scholars compare versions systematically through collation, 
  	which is typically carried out manually and is tedious and error-prone, 
  	with results that often need to be checked more than once (Haentjens Dekker et al., 2015; Nury, 2018).
  * Readers who simply want to find how a passage appears in other versions face a similar burden, 
  	as they must locate its counterparts by hand.
  * Computational support therefore has the potential to reduce a substantial burden.


  (low-resources languages, medieval irish, gap:technical expertise, resources)
  * However, computational resources and methods remain scarce for low-resource languages (Joshi et al., 2020),
    and historical languages are among the most affected (Dereza et al., 2024).
  <!-- * We use Medieval Irish as a case study. It has a rich literary tradition,  --> as an example, 
  	yet few computational resources are available for it (Doyle and McCrae, 2024),
  	and its narratives survive in versions ranging from Medieval to Modern Irish, 
  	whose spelling changed considerably over time (Cnockaert-Guillou, 2025).
  *	Computational methods for the language largely depend on annotated training data, 
  	which is scarce and inconsistent (Dereza, 2019; Doyle and McCrae, 2024).
  * Existing comparison tools, in turn, either require texts to be manually encoded or aligned in advance, 
  	demand technical expertise, or are designed to discover reuse across large corpora rather than to compare versions of the same 	   text (see Section 2).
  * Although we focus on Medieval Irish, our approach does not depend on language-specific resources and 
  	is intended to be applicable to other low-resource languages.


2.Related Work
2.1 Historical Low-Resource Languages and Textual Variation
  - Two challenges: scarce resources; textual variation across versions
  - Challenge 1: Scarce resources
      1. Language technologies concentrated on a few languages (Joshi et al., 2020)
      2. Historical languages are an extreme case: corpora cannot be extended;
         even Latin and Ancient Greek lack material for some periods (Moritz et al., 2018)
      3. NLP models need large training data; evidence: best average accuracy only 5.95% (Dereza et al., 2024)
  - Challenge 2: Textual variation
      1. No standardised orthography, so spelling varies (Bollmann, 2019)
      2. Examples: Canterbury Tales, Nibelungenlied; differ in spelling and wording,
         which makes comparing versions hard
      3. Common solution: normalisation; limitation: costly manual data (Huang et al., 2023)
  - Medieval Irish (last paragraph)
      1. Existing tools already struggle with historical languages, even more so with Medieval Irish
      2. Resources: eDIL, CELT, UD Old Irish treebanks, POMIC
     	 Limitations: small, mostly Old Irish glosses,
      	 inconsistently annotated (Doyle and McCrae, 2024; Dereza, 2019)
      3. Variation goes further: Latin / Middle English variants stay recognisably similar;
         initial mutations and infixed pronouns change a word's beginning and interior
         (Doyle and McCrae, 2024; Doyle, 2024)
      4. So adapting tools would need even more costly manual work
  - Solution  we therefore use a training-free approach:
  <!-- 2.3 levenshtein distance and sliding window -->

 2.2 Tools for Reading and Comparing Text Versions
   - Tools
  	1, Manually comparing versions is laborious (Haentjens Dekker et al., 2015), 
  	   and severl tools support it, but each sets a barrier for users without technical expertise.
  	2, The Versioning Machine supports parallel reading of multiple versions, with synchronized scrolling and highlighting of
  	   corresponding units across versions (Schreibman, 2005). However, text sources must first be encodaed manually by an editor, 		   with all versions combined in a single TEI file.
    3, Collation tools such as CollateX compute differences automatically but have a    high entry barrier: from tokenisation and normalisation to the choice of alignment algorithm, users must make technical decisions, and full use requires Python or the command line (Haentjens Dekker et al., 2015). dekk
  	4, LERA lowers this barrier with an interactive interface, but its functions are designed around collation, and it involves many concepts and settings, such as normalisation, manual correction of alignments, word clouds and the CATview overview (Pöckelmann et al., 2023).
    5, Passage-matching tools such as TextPAIR and Tesserae come closest to retrieving similar passages, but they are designed to discover reuse across corpora: TextPAIR requires a command-line installation and computes all matches in advance (Olsen, Horton and Roe, 2011), while Tesserae is limited to its own Latin, Greek and English corpora (Coffee et al., 2012).

  - Medieval Irish 
  	1,In principle, language-independent tools such as CollateX and LERA can also be applied to Medieval Irish. In practice, however, the extensive spelling variation between Medieval and Modern Irish versions would have to be handled through user-defined normalisation rules, which require both linguistic and technical expertise.
    2,Tools that cope with variation through stemming or lemmatisation, such as TextPAIR and Tesserae, depend on resources that are not readily available for Medieval Irish (Doyle and McCrae, 2024).
    3,Readers therefore largely rely on keyword search in corpora such as CELT, which depends on the spelling used in the query.

  - Barrier
    1,These barriers matter because comparatively few humanities scholars use complex digital tools (Gibbs and Owens, 2012), and some still prefer manual comparison because they find existing tools inaccurate or cumbersome ([Virtual Hinman]).
    2,Scholars mainly use digital tools to speed up their existing research. They expect to work with their own sources, to use a tool without programming, to understand its output and to find clear, non-technical documentation, and they abandon tools whose benefit is not quickly apparent (Gibbs and Owens, 2012).
    3,Gibbs and Owens (2012) therefore argue for simple, intuitive tools that focus on a specific task rather than ever more sophisticated ones, and for tools that can import and export data so that they work alongside other tools and resources.

  Taken together, a tool supporting comparison across versions should focus on a single task in the reading workflow: retrieving corresponding passages on demand and presenting them across multiple versions simultaneously. It should work directly with users’ owntexts, require no programming or configuration, and produce results that are easy to interpret.


2.3 Training-Based and Training-Free Approaches
  - 2.1 ruled out, such as manually mapped spelling variants (Ernst-Gerlach and Fuhr, 2007) or normalisation tools such as VARD (Pilz et al., 2008). Approaches that avoid such resources fall into two groups: those that learn from training data and those that require no training at all.
  - Training-Based approaches
    1,Learned representations such as sentence embeddings avoid hand-crafted rules but depend on training data. Generic multilingual encoders transfer poorly to ancient languages, and labelled similarity data for them is unavailable (de la Selle, 2026).
    2,Even large language models that claim to cover Irish and Scottish Gaelic offer limited benefit: on Irish and Gaelic folktales, a simple baseline with non-contextual features performs comparably (Meaney et al., 2024).
    3,Such models also require more computational resources, are less interpretable and make results harder to reproduce (Wolf et al., 2024).
  - Training-free
    1,Lexical methods such as BM25 require no training and remain robust baselines across retrieval tasks (Thakur et al., 2021). However, they match identical word forms, so spelling variants of the same word are treated as different words.
    2,Approximate string matching based on edit distance instead measures how many changes turn one string into another (Levenshtein, 1966; Navarro, 2001). It tolerates spelling variation without training data or language-specific resources, and its results can be traced back to the differing characters.
   	3,Libraries such as fuzzy-search apply this idea to historical texts, but are intended for programmers rather than end users (Koolen, [2015]).

  - We therefore adopt a training-free approach that combines edit distance with a sliding window to locate corresponding passages in unsegmented text, and optimise it through pruning so that it remains fast on long texts (Section 4).
