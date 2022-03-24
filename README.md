===============================================================================

NEGES 2018 - Workshop on Negation in Spanish - Task 2: Negation cues detection
 
Training and development sets released: May 14, 2018.

Web site: http://www.sepln.org/workshops/neges/index.php?lang=en

------------------------------------
Organizing comittee
------------------------------------
Salud María Jiménez Zafra, sjzafra@ujaen.es (Universidad de Jaén, Spain)
Maite Martín Valdivia, maite@ujaen.es (Universidad de Jaén, Spain)
Noa Cruz Díaz, contact@noacruz.com (Savana Médica, Madrid, Spain)
Roser Morante, r.morantevallejo@vu.nl (VU Amsterdam, Netherlands)
===============================================================================


------------------------------------
CONTENT FOLDER
------------------------------------
The folder "task2" contains the training and development sets for Task 2 and the evaluation scripts.
The subfolder "corpus_SFU_Review_SP_NEG_task2" contains the corpus.
The subfolder "scorer" contains the evaluation script.


------------------------------------
TASK DESCRIPTION
------------------------------------
Task 2: Negation cues detection

The task consists in identifying negation cues automatically. To do this, participants must develop a system able to identify all the negation cues present in a document. The SFU ReviewSP-NEG corpus (Jiménez-Zafra et al., 2017) will be used to train and test the systems. Cues can be single words (e.g., "no"), multiwords (e.g., "ni siquiera") or discontinuous words (e.g., "no...apenas").


-------------
CORPUS 
-------------

The SFU ReviewSP-NEG corpus (Jiménez-Zafra et al., 2017) has been splitted into development, training and test sets. It is an extension of the Spanish part of the SFU Review corpus (Taboada et al., 2006) and it could be considered the counterpart of the SFU Review Corpus with negation and speculation annotations (Konstantinova et al., 2012). The Spanish SFU Review corpus consists of 400 reviews extracted from the website Ciao.es that belong to 8 different domains: cars, hotels, washing machines, books, cell phones, music, computers, and movies. For each domain there are 50 positive and 50 negative reviews, defined as positive or negative based on the number of stars given by the reviewer (1-2=negative; 4-5=positive; 3-star review were not included). Later, it was extended to the SFU ReviewSP-NEG corpus in which each review was automatically annotated at the token level with pos-tags and lemmas, and manually annotated at the sentence level with negation cues and their corresponding scopes and events. Moreover, it is the first corpus in which it was annotated how negation affects the words that are within its scope, that is, whether there is a change in the polarity or an increment or reduction of its value.

Training:  264 reviews, 33 per domain. It is provided one file per domain (cars, hotels, washing machines, books, cell phones, music, computers, and movies).

Development:  56 reviews, 7 per domain. It is provided one file per domain (cars, hotels, washing machines, books, cell phones, music, computers, and movies).


The corpus was automatically tokenized, PoS tagged and lemmatized using Freeling and then, it was manually annotated with negation and polarity information applying the procedure described in (Jiménez-Zafra et al., 2017).

Jiménez-Zafra, S. M., Taulé, M., Martín-Valdivia, M. T., Ureña-López, L. A., & Martí, M. A. (2017). SFU ReviewSP-NEG: a Spanish corpus annotated with negation for sentiment analysis. A typology of negation patterns. Language Resources and Evaluation, 1-37. https://doi.org/10.1007/s10579-017-9391-x

Konstantinova, N., & De Sousa, S. C. (2011). Annotating negation and speculation: the case of the review domain. In Proceedings of the Second Student Research Workshop associated with RANLP 2011 (pp. 139-144).

Taboada, M., Anthony, C., & Voll, K. (2006, May). Methods for creating semantic orientation dictionaries. In Conference on Language Resources and Evaluation (LREC) (pp. 427-432).


-------------
FORMAT
-------------

The data are provided in CoNLL format. Each line corresponds to a token and each annotation is provided in a column; empty lines indicate end of sentence. The content of the columns given is:


Column 1: domain_filename

Column 2: sentence number within domain_filename

Column 3: token number within sentence

Column 4: word

Column 5: lemma

Column 6: part-of-speech

Column 7: part-of-speech type


Systems have to output one file per domain with the contents of the following columns (the files must have the same order of sentences and tokens as the test files):


Columns 8 to last:

- If the sentence has no negations,  column 8 has a "***" value and there are no more columns.
- If the sentence has negations, the annotation for each negation is provided in three columns. The first column contains the word that belongs to the negation cue. The second and third column contains "-".

In Example 1 there is no negation so the 8th column is "***" for all tokens. Example 2 is a sentence with one negation cue and the information about negation is provided in colums 8-10. Example 3 is a sentence with two negation cues in which information for the first negation is provided in columns 8-10, and for the second in columns 11-13. 

Example 1 - Sentence without negation: the 8th column is "***" for all tokens.

	hoteles_no_1_1	1	1	Me	me	pp1cs000	personal	***	
	hoteles_no_1_1	1	2	he	haber	vaip1s0	auxiliary	***	
	hoteles_no_1_1	1	3	alojado	alojar	vmp00sm	main	***	
	hoteles_no_1_1	1	4	en	en	sps00	preposition	***	
	hoteles_no_1_1	1	5	dos	2	z	-	***	
	hoteles_no_1_1	1	6	ocasiones	ocasión	ncfp000	common	***	
	hoteles_no_1_1	1	7	en	en	sps00	preposition	***	
	hoteles_no_1_1	1	8	este	este	dd0ms0	demonstrative	***	
	hoteles_no_1_1	1	9	hotel	hotel	ncms000	common	***	
	hoteles_no_1_1	1	10	,	,	fc	-	***	
	hoteles_no_1_1	1	11	y	y	cc	coordinating	***	
	hoteles_no_1_1	1	12	lo	el	da0ns0	article	***	
	hoteles_no_1_1	1	13	único	único	aq0ms0	qualificative	***	
	hoteles_no_1_1	1	14	que	que	pr0cn000	relative	***	
	hoteles_no_1_1	1	15	destaco	destacar	vmip1s0	main	***	
	hoteles_no_1_1	1	16	es	ser	vsip3s0	semiauxiliary	***	
	hoteles_no_1_1	1	17	su	su	dp3cs0	possessive	***	
	hoteles_no_1_1	1	18	ubicación	ubicación	ncfs000	common	***	
	hoteles_no_1_1	1	19	,	,	fc	-	***	
	hoteles_no_1_1	1	20	cerca	cerca	rg	-	***	
	hoteles_no_1_1	1	21	de	de	sps00	preposition	***	
	hoteles_no_1_1	1	22	Sol	sol	np00000	proper	***	
	hoteles_no_1_1	1	23	,	,	fc	-	***	
	hoteles_no_1_1	1	24	de	de	sps00	preposition	***	
	hoteles_no_1_1	1	25	la	el	da0fs0	article	***	
	hoteles_no_1_1	1	26	Gran_Vïa	gran_vïa	np00000	proper	***	
	hoteles_no_1_1	1	27	,	,	fc	-	***	
	hoteles_no_1_1	1	28	muy	muy	rg	-	***	
	hoteles_no_1_1	1	29	bien	bien	rg	-	***	
	hoteles_no_1_1	1	30	situado	situar	vmp00sm	main	***	
	hoteles_no_1_1	1	31	.	.	fp	-	***

Example 2 - Sentence with negation: the columns for negation start at the 8th columns. There will be three columns for each negation (cue, -, -) and three colums for each token that is not a negation cue (-, -, -).

	hoteles_no_1_4	11	1	Me	me	pp1cs000	personal	-	-	-	
	hoteles_no_1_4	11	2	quedé	quedar	vmis1s0	main	-	-	-	
	hoteles_no_1_4	11	3	pensando	pensar	vmg0000	main	-	-	-	
	hoteles_no_1_4	11	4	como	como	cs	subordinating	-	-	-	
	hoteles_no_1_4	11	5	seria	seriar	vmip3s0	main	-	-	-	
	hoteles_no_1_4	11	6	para	para	sps00	preposition	-	-	-	
	hoteles_no_1_4	11	7	un	uno	di0ms0	indefinite	-	-	-	
	hoteles_no_1_4	11	8	minusválido	minusválido	ncms000	common	-	-	-	
	hoteles_no_1_4	11	9	tener	tener	vmn0000	main	-	-	-	
	hoteles_no_1_4	11	10	que	que	cs	subordinating	-	-	-	
	hoteles_no_1_4	11	11	subir	subir	vmn0000	main	-	-	-	
	hoteles_no_1_4	11	12	aquellas	aquel	dd0fp0	demonstrative	-	-	-	
	hoteles_no_1_4	11	13	escaleras	escalera	ncfp000	common	-	-	-	
	hoteles_no_1_4	11	14	mal	mal	rg	-	-	-	-	
	hoteles_no_1_4	11	15	hechas	hacer	vmp00pf	main	-	-	-	
	hoteles_no_1_4	11	16	y	y	cc	coordinating	-	-	-	
	hoteles_no_1_4	11	17	sin	sin	sps00	preposition	sin	-	-	
	hoteles_no_1_4	11	18	rampa	rampa	ncfs000	common	-	-	-	
	hoteles_no_1_4	11	19	.	.	fp	-	-	-	-

Example 3 - Sentence with two negations: the information for the first negation is provided in columns 8-10, and for the second in columns 11-13. There will be three columns for each negation (cue, -, -) and three colums for each token that is not a negation cue (-, -, -).

	hoteles_no_2_6	9	1	Aun	aun	np00000	proper	-	-	-	-	-	-	
	hoteles_no_2_6	9	2	estoy	estar	vaip1s0	auxiliary	-	-	-	-	-	-	
	hoteles_no_2_6	9	3	esperando	esperar	vmg0000	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	4	que	que	cs	subordinating	-	-	-	-	-	-	
	hoteles_no_2_6	9	5	me	me	pp1cs000	personal	-	-	-	-	-	-	
	hoteles_no_2_6	9	6	carguen	cargar	vmsp3p0	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	7	los	el	da0mp0	article	-	-	-	-	-	-	
	hoteles_no_2_6	9	8	puntos	punto	ncmp000	common	-	-	-	-	-	-	
	hoteles_no_2_6	9	9	en	en	sps00	preposition	-	-	-	-	-	-	
	hoteles_no_2_6	9	10	mi	mi	dp1css	possessive	-	-	-	-	-	-	
	hoteles_no_2_6	9	11	tarjeta	tarjeta	ncfs000	common	-	-	-	-	-	-	
	hoteles_no_2_6	9	12	más	más	rg	-	-	-	-	-	-	-	
	hoteles_no_2_6	9	13	,	,	fc	-	-	-	-	-	-	-	
	hoteles_no_2_6	9	14	no	no	rn	negative	no	-	-	-	-	-	
	hoteles_no_2_6	9	15	sé	saber	vmip1s0	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	16	dónde	dónde	pt000000	interrogative	-	-	-	-	-	-	
	hoteles_no_2_6	9	17	tienen	tener	vmip3p0	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	18	la	el	da0fs0	article	-	-	-	-	-	-	
	hoteles_no_2_6	9	19	cabeza	cabeza	ncfs000	common	-	-	-	-	-	-	
	hoteles_no_2_6	9	20	pero	pero	cc	coordinating	-	-	-	-	-	-	
	hoteles_no_2_6	9	21	no	no	rn	negative	-	-	-	no	-	-	
	hoteles_no_2_6	9	22	la	lo	pp3fsa00	personal	-	-	-	-	-	-	
	hoteles_no_2_6	9	23	tienen	tener	vmip3p0	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	24	donde	donde	pr000000	relative	-	-	-	-	-	-	
	hoteles_no_2_6	9	25	deberían	deber	vmic3p0	main	-	-	-	-	-	-	
	hoteles_no_2_6	9	26	.	.	fp	-	-	-	-	-	-	-	


------------
EVALUATION
------------

The evaluation script provided is the one used in *SEM 2012 Shared Task - Resolving the Scope and Focus of Negation (Morante and Blanco, 2012). It was developed by Roser Morante and is based on the following criteria:

- Punctuation tokens are ignored.

- A true positive (TP) requires all tokens of the negation element have to be correctly identified. 

- To evaluate cues, partial matches are not counted as FP, only as FN. This is to avoid penalizing partial matches more than missed matches. 


The following evaluation measures are used to evaluate the systems:

- Cue-level precision.
- Cue-level recall.
- Cue-level F1-measure.
- Percentage of correct negation sentences.

 precision = tp / (tp + fp)
 recall = tp / (tp + fn)
 F1 = (2 * $precision_cue * $recall_cue) / ($precision_cue + $recall_cue)

 False negatives are counted either by the system not identifying negation elements present in gold, or by identifying them partially, i.e., not all tokens have been correctly identified or the word forms are incorrect.

 False positives are counted when the system produces a negation element not present in gold.

 True positives are counted when the system produces negation elements exactly as they are in gold.

 Example 1:

 Gold annotation: cue is "ni siquiera".
 System output: cue is "ni".
 Cue will be false negative because not all tokens have been produced by system.

 Example 2:

 Gold doesn't have a negation.
 System produces a negation, then the negation cue produced by system will count as false positive.

 Example 3:

 Gold annotation: cue is "no".
 System output: cue is "no".
 Cue will be true positive because negation cue have been produced as it is in gold.

A second version of the  measures (B) is provided to participants. In the B version of the measures, precision is not counted as (TP/(TP+FP)), but as  (TP / total of system predictions), counting in this way the percentage of perfect matches among all the system predictions.


For evaluating, use the file scorer_task2.pl. You can execute this perl command with -h to obtain help:

>perl scorer_task2.pl -h

Usage: [perl] scorer_task2.pl [OPTIONS] -g <gold standard> -s <system output>

Options:
      -h : help:        print this help text and exit
       -r : readme:      print a brief explanation about the evaluation output

More details about the evaluation are provided in Morante and Blanco (2012).


-------------
REFERENCES
-------------

Jiménez-Zafra, S. M., Taulé, M., Martín-Valdivia, M. T., Ureña-López, L. A., & Martí, M. A. (2017). SFU ReviewSP-NEG: a Spanish corpus annotated with negation for sentiment analysis. A typology of negation patterns. Language Resources and Evaluation, 1-37. https://doi.org/10.1007/s10579-017-9391-x

Morante R. and Blanco E. (2012). *SEM 2012 Shared Task: Resolving the Scope and Focus of Negation. In Proceeding of the First Joint Conference on Lexical and Computational Semantics. Montreal, Canada

Jiménez-Zafra, S. M., Martin, M., Lopez, L. A. U., Marti, T., & Taulé, M. (2016). Problematic cases in the annotation of negation in Spanish. In Proceedings of the Workshop on Extra-Propositional Aspects of Meaning in Computational Linguistics (ExProM) (pp. 42-48).

Martí, M. A., Martín-Valdivia, M. T., Taulé, M., Jiménez-Zafra, S. M., Nofre, M., & Marsó, L. (2016). La negación en español: análisis y tipología de patrones de negación. Procesamiento del Lenguaje Natural, 57, 41-48.

