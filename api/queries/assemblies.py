"""API utilities for Assembly related viewsets."""
from api.utils import query_database
import json


def get_assembly_stats(sample_id, user_id, is_plasmids=None):
    """Return assembly stats for a set of sample ids."""
    cols = [
        'sample_id', 'total_contig',  'total_contig_length',
        'min_contig_length', 'median_contig_length', 'mean_contig_length',
        'max_contig_length', 'n50_contig_length',
        'l50_contig_count', 'ng50_contig_length', 'lg50_contig_count',
        'contigs_greater_1k', 'contigs_greater_10k', 'contigs_greater_100k',
        'contigs_greater_1m', 'percent_contigs_greater_1k',
        'percent_contigs_greater_10k', 'percent_contigs_greater_100k',
        'percent_contigs_greater_1m', 'contig_percent_a', 'contig_percent_t',
        'contig_percent_g', 'contig_percent_c', 'contig_percent_n',
        'contig_non_acgtn', 'num_contig_non_acgtn'
    ]

    table = 'plasmid_summary' if is_plasmids else 'assembly_summary'
    sql = """SELECT {0}
             FROM {1} AS a
             LEFT JOIN sample_sample as s
             ON s.id=a.sample_id
             WHERE sample_id IN ({2}) USER_PERMISSION
             ORDER BY sample_id;""".format(
        ','.join(cols),
        table,
        ','.join([str(i) for i in sample_id])
    )

    return query_database(sql)


def get_assembly_contigs(sample_id, user_id, is_plasmids=False, contig=None,
                         exclude_sequence=False):
    """Return assembled contigs for a set of sample ids."""
    # Get contigs
    table = 'plasmid_sequence' if is_plasmids else 'assembly_sequence'
    sql = """SELECT c.sample_id, c.fasta
             FROM {0} AS c
             LEFT JOIN sample_sample as s
             ON s.id=c.sample_id
             WHERE c.sample_id IN ({1}) USER_PERMISSION
             ORDER BY sample_id ASC;""".format(
        table,
        ','.join([str(i) for i in sample_id])
    )
    results = []
    contigs = {}
    for row in query_database(sql):
        contigs[row['sample_id']] = row['fasta']

    # Get contig names
    names = {}
    table = 'plasmid_contig' if is_plasmids else 'assembly_contig'
    sql = """SELECT sample_id, spades, staphopia
             FROM {0} AS c
             LEFT JOIN sample_sample as s
             ON s.id=c.sample_id
             WHERE c.sample_id IN ({1}) USER_PERMISSION
             ORDER BY sample_id ASC, c.id ASC;""".format(
        table,
        ','.join([str(i) for i in sample_id])
    )
    for row in query_database(sql):
        # Spades: NODE_37_length_341_cov_381.897727
        cols = row['spades'].split("_")
        sequence = None
        if contig and int(cols[1]) != contig:
            continue

        if is_plasmids:
            sequence = contigs[row['sample_id']][row['staphopia']]
        else:
            sequence = contigs[row['sample_id']][cols[1]]

        if exclude_sequence:
            sequence = ''

        results.append({
            'sample_id': row['sample_id'],
            'contig': cols[1],
            'header': row['staphopia'],
            'coverage': float(f'{float(cols[5]):.2f}'),
            'length': int(cols[3]),
            'sequence': sequence
        })

    return results
