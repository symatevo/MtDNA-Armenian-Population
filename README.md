# Human Mitochondrial DNA Analysis

This project focuses on the analysis of human mitochondrial DNA (mtDNA) to explore genetic variations within the Armenian and it's neighbouring populations. The project encompasses various stages, including data preprocessing, alignment, variant calling, annotation, haplogroup determination, phylogenetic tree construction and clustering analysis.

## Team

- Syuzi Matevosyan (syuzi.matevosyan1802@gmail.com)
- Arpine Griogoryan (arpigrigoryan1@gmail.com)

## Workflow

### 0. Preprocessing

Fasta files for each sample were acquired and organized using the `download_fasta.py` script located in the `scr/preprocessing` directory. The data is stored in the `mt_fastas/samples` directory.

### 1. Alignment and Variant Calling

For the alignment process, BWA (Version: 0.7.17-r1188) was employed with the `alignment.sh` script found in the `scr/preprocessing` directory. The rCRS (NC_012920) was utilized as the reference genome. The script conducts alignment, stores the results in the `/sam` directory, and subsequently performs variant calling for each sample. The variant calling process utilized BCFtools call (Version: 1.16), and the resulting Variant Call Format (VCF) files are stored in the `vcfs/` directory.

### 2. Variant Annotation

The annotation of variants was accomplished using snpEff (Version: 5.1d). Initially, a human mitochondrial library was constructed using a gff3 file obtained from GenBank. The annotation script `annotation.sh` (located in `scr`) was then executed. The annotated VCF files are stored in the `/anno` directory.

### 3. Defining Haplogroups

Haplogroups were determined using the HaploGrep web server (Version 3.0) accessible at [https://haplogrep.i-med.ac.at/](https://haplogrep.i-med.ac.at/). The results were downloaded and saved as a zip file named `haplogroups.zip`.

### Data Sources

1. **Paper:** Derenko et al. (2019) Insights into matrilineal genetic structure, differentiation, and ancestry of Armenians based on complete mitogenome data.
   - [Read the paper](https://doi.org/10.1007/s00438-019-01596-2)
   - Samples: Complete human mitogenomes, GenBank accession numbers: MK491355–MK491495

2. **Paper:** Derenko, M. et al. (2013) Complete mitochondrial DNA diversity in Iranians. (355 Iranian, Kurd, Russian, Qashqai mtDNAs)
   - [Read the paper](https://doi.org/10.1371/journal.pone.0080673)

3. **Paper:** Schoenberg, A. et al. (2011) High-throughput sequencing of complete human mtDNA genomes from the Caucasus and West Asia: high diversity and demographic inferences.
   - [Read the paper](https://doi.org/10.1038/ejhg.2011.62)

4. **Paper:** Ashot Margaryan, Miroslava Derenko (2017) Eight Millennia of Matrilineal Genetic Continuity in the South Caucasus
   - [Read the paper](http://dx.doi.org/10.1016/j.cub.2017.05.087)

### 4. Building a Phylogenetic Tree

For constructing the phylogenetic tree, coding sequences were utilized. This involved transforming the gff3 genome annotation file from NCBI to a BED file using Bedops' gff2bed tool. Protein-coding regions were then extracted from samples using Bedtools. The sequences of each protein across all samples were aligned, and based on this alignment, phylogenetic trees were built. The following scripts were used:

- `scr/coding_regions_test.sh`: Extracts coding regions.
- `scr/building_phylo_tree.sh`: Builds phylogenetic trees based on each protein within populations.
- `scr/prot_across_samples.sh`: Builds a phylogenetic tree based on proteins across populations.
- `scr/phylo_tree_whole_genome.sh`: Builds a phylogenetic tree based on whole genome data.

### 5. Clustering Analysis

Our first step in clustering analysis was matrix generation that represents the presence or absence of mutations in specific genes across different samples. A value of '1' signifies the presence of a mutation, while '0' indicates its absence. To get initial understanding of the genetic variation among samples this matrix was visualized. ATP and CYTB gene mutations were present in all samples. Distributations of mutations in ATP and CYTB were visualized.
K-means clustering analyse performed on the mutation matrix, using 'k = 3' as the number of clusters.To facilitate the interpretation of clustering results, Principal Component Analysis (PCA) were used. This technique reduces the dimensionality of the data while preserving as much variance as possible. By visualizing the samples in a lower-dimensional space, we aimed to identify any clear separation or clustering among the populations. The following scripts were used:

- `clustering/matrix_sample_gene.py`: Generates matrix.
- `clustering/metadata_sample_nationality.py`: Generates metadata.
- `clustering/clustering.ipynb`: Performes clustering analysis and visualization.

(add distribution samples population, samples mutations)
1. Sui(Our results revealed that Guangxi and Guizhou Sui people showed a strong genetic affinity with populations from southern China and Southeast Asia, especially Tai-Kadai- and Hmong-Mien-speaking populations as well as ancient Iron Age Taiwan Hanben, Gongguan individuals supporting the hypothesis that Sui people came from southern China originally. Guizhou Sui people were relatively homogeneous and possessed similar genetic profiles with neighboring Tai-Kadai-related populations, such as Maonan. While Sui people in Yizhou and Huanjiang of Guangxi might receive unique, additional gene flow from Hmong-Mien-speaking populations and Northern East Asians, respectively, after the divergence within other Sui populations. ), nice georgraphic not extremely diverse from Armenians
Data obtained from ON983561 - ON983657 (biggest minus is data UNVERIFIED)

2. Bouyei (homogenous), Dong (not available)
3. Hakka Han - Pingtung, Taiwan, China KF540656-KF540700
   Minnan Han - Kaohsiung, Taiwan, China KF540701-KF540750
A large-scale genetic study suggests that Han Chinese, including Hakka Han, are genetically homogeneous with differences largely based on geographic residence in northern versus southern regions7.
