# adb-vcftools

### How to install

* Clone the repository
```
git clone https://github.com/adbharadwaj/adb-vcftools.git
```
* In the command line, enter the cloned repository
```
cd adb-vcftools
```
* Install [python](http://www.tutorialspoint.com/python/python_environment.htm) if not installed
* Install [pip](http://pip.readthedocs.org/en/stable/installing/) if not installed. For Mac users:
```
brew install pip
```
* Install the command line tool
```
pip install --editable .                                                                   
```
* Activate the command line tool for current bash session
```
source venv/bin/activate  
```
### How to Use

Basic useful feature list:

 * Extend the functionality offered by [vcftools](https://vcftools.github.io/index.html).
 * Create command line tools which can convert any vcf file into [TASSEL](https://bytebucket.org/tasseladmin/tassel-5-source/wiki/docs/Tassel5PipelineCLI.pdf). compatible vcf file.

Current Version: 0.1.0

Here is a list of commands available in version 0.1.0:
 * duplicate 
 * fix_haploids 

And here is an example on how to use these commands:

### fix_haploids
```
Usage: adb-vcftools fix_haploids [OPTIONS]

  Convert the haploid genotype to homozygous diploids.

  It will convert 0 to 0/0 or 1 to 1/1. This is useful for programs which do
  not handle haploid genotypes correctly. For example: TASSEL

  Sample Usage:

  adb-vcftools fix_haploids --input sampledata/example-1.vcf --output
  sampledata/out-fixed-haploids-example-1.vcf

Options:
  --input PATH   Input VCF file  [required]
  --output PATH  Output VCF file  [required]
  --help         Show this message and exit.
```

### duplicate
```
Usage: adb-vcftools duplicate [OPTIONS]

  Create a duplicate copy of input file and save it as given output file.

  Sample Usage:

  adb-vcftools duplicate --input sampledata/example-1.vcf --output
  sampledata/out-duplicate-example-1.vcf

Options:
  --input PATH   Input VCF file  [required]
  --output PATH  Output VCF file  [required]
  --help         Show this message and exit.
```
### Python packages used in thie project:

 * [pyvcf](http://pyvcf.readthedocs.org/en/latest/index.html) for VCF parsing
 * [click](http://click.pocoo.org/) for creating the command line interface
