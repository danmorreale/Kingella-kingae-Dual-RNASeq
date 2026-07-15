# _Kingella kingae_ Dual RNA-Seq
Molecular determinants of Kingella kingae translocation across polarized respiratory epithelium

DOI:  [![DOI](https://zenodo.org/badge/647272024.svg)](https://doi.org/10.5281/zenodo.21384628)

Authors: Morreale, Daniel P., Ana K. Cruz, Porsch, Eric A., Eva Agostino, Planet, Paul J, St. Geme III, Joseph W.

University of Pennsylvania
Childrens Hospital of Philadelphia

Please contact D. Morreale or J. St. Geme III with questions/concerns.

 
## Background 
This repository contains the data and code used for the analysis of the Dual-RNA seq data reported in "Molecular determinants of Kingella kingae translocation across polarized respiratory epithelium". Below you will find a detailed methods section for the analysis, which can also be found in the manuscript. Read data can be found in the Gene Expression Omnibus GSE334948. Please contact the authors with any questions/concerns. 


## Methods
### Sample preparation
#### Tissue and Bacterial Culture
Calu-3 cells were obtained from the American Tissue Culture collection (ATCC HTB-55, human lung adenocarcinoma). Cells were grown and maintianed in culture media 1x EMEM (Corning REF. #10-009-CV) supplemented with 10% fetal bovine serum (FBS), without antibiotics, and maintained in a humidified 37 C incubator with 5% CO2. To generate semi-differentiated culutres,24-well ThinCert transwell supports (Greiner Bio-One, 3.0 μm pore, REF. #662630) were seeded with 2e5 cells. Prior to seeding cells, the transwell supports were pre-coated with a mixture of extracellular matrix components containing collagen, fibronectin, and bovine serum antigen in 1x EMEM for 2 hrs. Calu-3 cells were cultured on the transwell support, sub-liquid, for 5 days to allow for proper adherence and for the cells to reach confluency. After 5 days, the apical media was removed, and the basolateral media was replaced every other day for 3 weeks (20-23 days) with pre-warmed 1x EMEM + 10% FBS. Prior to infection, the transepithelial resistance of each culture was measured to ensure the proper formation of tight junctions, an indication of proper differentiation. Culutres were used for experiments if TEER > 800Ω. 

_Kingella kingae_ strain KK01 was grown for 20 hrs on chocolate agar at 37 C with 5% CO2. Bacterial growth was collected and resuspended in heart infusion broth to an OD 600 ~ 0.8. 
 
#### Infection
At the time of infection, differentiated Calu-3 cultures were transferred to prewarmed 1x EMEM without additional FBS. 10 μL of resuspended bacterial culture (1e6 CFU) was added to 100 μL of 1x EMEM, and this mixture was infected into the apical chamber. For the bacterial-only control, 40 μL of bacterial culture was infected into a well containing only 400 μL of 1x EMEM. For the uninfected control, the apical chamber received the same volume of 1x EMEM + 10 μL of sterile heart infusion broth. Cultures were maintained in a humidified 37 C incubator with 5% CO2 during the course of experimentation. Each condition was performed in duplicate (n=2) across 4, independent replicates (N=4).
 
#### RNA Extraction
At each time point, RNA was extracted as follows. Apical and basolateral media was collected and transferred into a sterile microcentrifuge tube for each well, respectively, and centrifuged for 5 min at >21k x _g_. After centrifugation, the supernatant was removed and discarded. Simultaneously, 1 mL of TRIzol reagent (Ambion Ref. #15596018) was added to the apical (~200 μL) and basolateral chamber (~800 μL), and incubated at room temperature (RT) for 5 mins. Samples were mixed by vigorous pipetting, and the TRIzol was removed to the matching tube. Samples were mixed again by pipetting. To facilitate complete bacterial and Calu-3 cell lysis, samples were incubated for 10 mins at RT for 10 mins. RNA was extracted following manufacturer's protocols. Final RNA pellets were resuspended in 100 μL of nuclease-free water (Thermoscientific Ref. #R0581) plus RNasin RNase inhibitor (Promega REF. # N261B).

To ensure all contaminating DNA was removed, each sample was treated twice with 12 U of RNase-free DNase I (Thermoscientific Ref. #01130383) for 1 hr at 37 C. **Complete DNA removal was verified by qPCR against GAPDH for btoh human and bacterial samples. **

Following DNase treatment, RNA was re-extracted via the RNeasy Mini Kit (Qiagen REF. #74104), following the manufacturer's "RNA Clean-up" protocol. RNA was into a final volume of 50 μL of nuclease-free water and stored at -80 C.

Duplicate samples (technical replicates) were pooled for quality control and library preparation. RNA integrity was measured using TapeStations High Sensitivity RNA ScreenTape (Aligent). RNA concentrations were quantified using a Qubi (ThermoScientific). 

|Tube Number|Sample ID|Hours Post Infection|RNA Source Organism (Bacterial/Human/Both)|RIN|RNA Concentration (ng/μL)| Replicate Number|
|---|---|---|---|---|---|---|
|1|1_B1|1|Bacterial|7.7|6.2|1|
|2|1_I1|1|Both|5.2|31.6|1|
|3|1_C1|1|Human|4.8|40|1|
|4|1_B8|8|Bacterial|8.2|15.8|1|
|5|1_I8|8|Both|6.1|34|1|
|6|1_C8|8|Human|6.5|30|1|
|7|1_B14|14|Bacterial|7.3|23.6|1|
|8|1_I14|14|Both|5.5|37.2|1|
|9|1_C14|14|Human|6.1|22|1|
|10|2_B1|1|Bacterial|8.7|3.57|2|
|11|2_I1|1|Both|7.5|22.1|2|
|12|2_C1|1|Human|7.3|24|2|
|13|2_B8|8|Bacterial|8.8|16.5|2|
|14|2_I8|8|Both|7.1|25.2|2|
|15|2_C8|8|Human|7.1|24.7|2|
|16|2_B14|14|Bacterial|8.3|7.53|2|
|17|2_I14|14|Both|6.8|15.3|2|
|18|2_C14|14|Human|7.4|19.2|2|
|19|3_B1|1|Bacterial|8.8|1.34*|3|
|20|3_I1|1|Both|7.3|21|3|
|21|3_C1|1|Human|7.4|21.7|3|
|22|3_B8|8|Bacterial|8.9|8.15|3|
|23|3_I8|8|Both|7.1|18|3|
|24|3_C8|8|Human|7.9|11.8|3|
|25|3_B14|14|Bacterial|8.4|10.2|3|
|26|3_I14|14|Both|6.5|15.7|3|
|27|3_C14|14|Human|7.4|22.2|3|
|28|4_B1|1|Bacterial|8.4|3.89|4|
|29|4_I1|1|Both|5.7|27.8|4|
|30|4_C1|1|Human|5.7|27.1|4|
|31|4_B8|8|Bacterial|8.3|12.4|4|
|32|4_I8|8|Both|5.5|27.4|4|
|33|4_C8|8|Human|5.8|26.3|4|
|34|4_B14|14|Bacterial|7.6|15.3|4|
|35|4_I14|14|Both|6|25.9|4|
|36|4_C14|14|Human|6.6|25.9|4|
||||||*From Tapestation||
### Library Preparation and Sequencing
Sequencing libraries were prepared from 10 ng of input RNA. Libraries were constructed using the Takara-Clontech total RNA pico mammalian v3 kit. Samples were fragmented with Clontech SMART-Seq HT kit (Takara), and SMARTScript reverse transcriptase was used for first strand synthesis with random primers. cDNA libraries were indexed prior to clean-up by AMPure beads purificaiton. Ribosomal cDNAs were depleted with ZapR and R-Probes v2. SeqAMP was used to amplify the final cDNA libraries. Library quality and concentrations were quantified with the TapeStation HSD1000 kit and Qubit HS dsDNA kit, respectively.

Sequencing was perforemd on the NovaSeq 2000 (Illumina). Samples were normalized by input cDNA, and run on a P3 100 cycle kit using single end 120x8x8 reads (120 bp single end reads, 8 bp dual indexes). 

### Bioinformatics
#### Reference genomes
KK01 is a stable colony variant recovered from the invasive strain 269-492, and the reference strains for work performed in the St. Geme lab. It was first isolated and described in “Identification and Characterization of an RTX Toxin in the Emerging Pathogen Kingella kingae” (Kehl-Fie & St. Geme III, 2007). KK01 underwent whole genome sequencing at CHOP in summer 2019 from gDNA of low passage stocks. Paired-end Illumina sequencing was performed.
Quality of sequences was assessed using FastQC v. 0.12.1. Trimming and assembly were performed simultaneously using the Shovill assembler v. 0.9.0. Assembly was performed with defaul options plus the following two flags: --minlen 200 --opts “-m 1024” – force
Final annotations were produced using Bakta v. 1.7.0. The full bakta database (v.5.0) was downloaded on 3/31/2023. Annotation was performed with the following flags:--prefix KK01 -- genus Kingella --species kingae --strain KK01 --gram ? --locus-tag KK01 -t 8.

#### Read sorting and quality control
Reads were uploaded to NCBI GEO GSE334948. All samples were treated identically, regardless of the species we expected to find, until human and bacterial reads were separated. Reads underwent quality control with FastQC. To remove any potential contamination from sequence or library preparation, FastQ Screen was used to label and sort reads against the human genome, KK01 genome, and phiX, using default setting and the Bowtie2 aligner. Tagged reads were then sorted as follows: Infected samples were separated into reads that map exclusively to the KK01 predicted transcriptome and Human transcriptome (GRCh38), respectively. Uninfected controls were filtered to remove any reads that do not map to the human reference (GRCh38). Bacterial-only controls were filtered to remove any reads that do not map to the KK01 reference. 

Kallisto (v.0.48.0) was used to pseudoalign filtered reads to the human reference transcriptome (GRCh38, index downloaded directly from Kallisto documentation) or the KK01 genome. Reads not mapping to either genome were ingored during mapping and all subsequent analyses.

#### Differential Expression
Kalisto output files were imported for subsequent analysis in R Studio with the tximport package (v.1.26.1). Human reads were analyzed interactively with the "Human_pipe.R" pipeline and bacterial reads were analyized with the "bacterial_pipeline.R" pipeline. 

For both species, data were grouped by replicate, treatment (+/- KK01), and hours post infection (h.p.i.). CPM from Kallisto were normalized to were normalize by TMM with edgeR (v.3.40.2). Limma (v.3.45.2) was used to fit calculate the mean-variance trend of the data and bayesian statistics were calculated. Prior to calculating differentially expessed genes, replicates were averaged by time-point. Finally, to generate differentially expressed gene lists, genes with Benjamini-Hochberg corrected p-values<0.05 with a fold change of at least 2 between conditions of interest were considered statistically significant. Plots were generated with ggplot2 (v.3.4.2). The following comparisons of interest were analyzed for both human and bacterial samples: 1 h.p.i Infected vs Control, 8 h.p.i Infected vs Control, 14 h.p.i Infected vs Control, 8 h.p.i Infected vs 1 h.p.i., and 8 h.p.i Infected vs 1 h.p.i. When comparing different time-points, the infected condition was normalized to the uninfected control prior to calculating differentially expressed genes. For human samples, transcript identifiers were converted to gene names from the EnsDb.Hsapiens.v86 (v.2.99.0) database. For bacterial samples, transcript identifiers were converted to gene names using the datafile (./KK01_genome/KK01.tsv) generated by Bakta.


## File Guide
### ./KK01_genome
#### Bakta files
- ./KK01_genome/KK01.ffn -- Bakta output file containing all conding sequences in FASTA format.
- ./KK01_genome/KK01.tsv -- Bakta output file containing complete annotation informaiton for mapping gene symbols to locus tags.
- ./KK01_genome/KK01.txt -- Bakta output file containing annotation statistics.

#### Kallisto Inputs
- ./KK01_genome/KK01_kallisto_index.idx -- Kallisto index for the mapping of reads specific to _K. kingae_ KK01.
### ./scripts
#### Shell/Python
- ./scripts/fastq_screen.sh -- Commands used for Fastq screen sorting of mixed reads.
- ./scripts/kallisto.sh -- Commands used to map and to human and KK01 indicies, respectively, for downstream analysis.
- ./scripts/collect.py -- Python script used to convert locus tags for bacterial genes into gene symbols after differential expression analysis.
- ./scripts/multiqc_report.html -- MultiQC report for all CLI tools.

#### R scripts
- ./scripts/bacterial_pipeline.R -- R Script used to analyse bacterial-specific reads for differential expression alaysis and graphics.
- ./scripts/Human_pipe.R -- R Script used to analyse Calu-specific reads for differential expression alaysis and graphics.

## Acknowledgments 
We would like to thank Clara Malekshahi and Daniel Beiting for their assistance with library preparation and seuqencing. Sequencing was performed in collaboration with the Center for Host-Microbial Interations at the University of Pennsylvania School of Veterinary Medicine. R-Scripts used for this analysis were originally written by D. Beiting as part of the curriculum for the [DIYTranscriptomics](https://diytranscriptomics.com/) course. Sections are heavily modified to accomodate our experimental design and several analyses have been added to address specific questions. 
