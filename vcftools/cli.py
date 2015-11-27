import click
import vcf

__author__ = 'adb'


class Config(object):

    def __init__(self):
        self.verbose = False

from collections import namedtuple
def convert(dictionary):
    return namedtuple('CallData', dictionary.keys())(**dictionary)

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def main(config, verbose):
    config.verbose = verbose


@main.command()
@click.option('--input', help='Input VCF file', type=click.Path(exists=True), required=True)
@click.option('--output', help='Output VCF file', type=click.Path(), required=True)
@pass_config
def duplicate(config, input, output):
    """
    Create a duplicate copy of input file and save it as given output file.

    \b
    Sample Usage:

    adb-vcftools duplicate --input sampledata/example-1.vcf --output sampledata/out-duplicate-example-1.vcf
    """
    if config.verbose:
        click.echo('We are in verbose mode')
    vcf_reader = vcf.Reader(filename=input)
    vcf_writer = vcf.Writer(open(output, 'w'), vcf_reader)
    for record in vcf_reader:
        vcf_writer.write_record(record)


@main.command()
@click.option('--input', help='Input VCF file', type=click.Path(exists=True), required=True)
@click.option('--output', help='Output VCF file', type=click.Path(), required=True)
@pass_config
def fix_haploids(config, input, output):
    """
    Convert the haploid genotype to homozygous diploids.

    It will convert 0 to 0/0 or 1 to 1/1.
    This is useful for programs which do not handle haploid genotypes correctly. For example: TASSEL

    \b
    Sample Usage:

    adb-vcftools fix_haploids --input sampledata/example-1.vcf --output sampledata/out-fixed-haploids-example-1.vcf

    """
    if config.verbose:
        click.echo('We are in verbose mode')
    vcf_reader = vcf.Reader(filename=input)
    vcf_writer = vcf.Writer(open(output, 'w'), vcf_reader)
    for record in vcf_reader:
        new_samples = []
        for call in record.samples:
            d = call.data._asdict()
            if d['GT'] and len(d['GT']) == 1:
                d['GT'] = '%s/%s' % (d['GT'], d['GT'])
                new_call = vcf.model._Call(call.site, call.sample, convert(d))
                new_samples.append(new_call)
            else:
                new_samples.append(call)

        r = vcf.model._Record(record.CHROM, record.POS, record.ID, record.REF, record.ALT, record.QUAL, record.FILTER, record.INFO, record.FORMAT, record._sample_indexes, samples=new_samples)
        vcf_writer.write_record(r)
