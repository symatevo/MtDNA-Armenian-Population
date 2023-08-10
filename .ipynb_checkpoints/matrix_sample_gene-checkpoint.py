import pandas as pd
import gzip
import re

# Function to extract VCF column names from a gzipped VCF file
def get_vcf_names(vcf_path):
    with gzip.open(vcf_path, "rt") as ifile:
        for line in ifile:
            if line.startswith("#CHROM"):
                vcf_names = [x for x in line.split('\t')]
                break
    ifile.close()
    return vcf_names

# Function to create a DataFrame from a gzipped VCF file

def create_vcf(vcf_path):
    vcf = pd.read_csv(vcf_path, compression='gzip', comment='#', delim_whitespace=True, header=None, names=names)
    return vcf

# List of target genes

genes = ["ND1", "ND2", "COX1", "COX2", "ATP6", "ATP8", "ND3", "ND4", "ND4L", "ND5", "ND6", "CYTB", "COX3"]

# Lists to store patient IDs and corresponding VCF file paths

patients = []
path_name = []

# Generate patient IDs and VCF file paths

for i in range(355, 496):
    patients.append('MK491' + str(i)) 
    path_name.append('../samples/arm_samples/anno/MK491' + str(i) + '.vcf.anno.vcf.gz')


# Create an empty DataFrame to store matrix data

matrix_data = pd.DataFrame(index=patients, columns=genes, dtype=int)
matrix_data = matrix_data.fillna(0)

# Function to find the first gene match in an input string

def find_first_gene_match(input_string):
    return next((gene for gene in genes if gene in input_string), None)


# Process each VCF file

for (file, patient) in zip(path_name, patients):
    names = get_vcf_names(file)  # Get VCF column names
    vcf = create_vcf(file)       # Create DataFrame from VCF file
    for gene in genes:
        # Check if gene is present in any INFO column, update matrix_data accordingly
        if (vcf["INFO"].apply(lambda x: find_first_gene_match(x)).str.contains(gene).sum() > 0):
            matrix_data.loc[patient].at[gene] = 1
        else:
            matrix_data.loc[patient].at[gene] = 0

# Uncomment these lines to save DataFrames to CSV files
# vcf.to_csv("out.csv")
#matrix_data.to_csv("matrix.csv")

# Display the resulting matrix_data DataFrame
print(matrix_data)
