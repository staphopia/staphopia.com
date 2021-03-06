"""API utilities for XYZ related viewsets."""
from collections import OrderedDict

from sccmec.tools import predict_type_by_primers, predict_subtype_by_primers

from api.utils import query_database


def get_sccmec_primers_by_sample(sample_id, user_id, is_subtypes=False,
                                 exact_hits=False, predict=False,
                                 hamming_distance=False):
    """Return SCCmec primer hits asscociated with a sample_id."""
    sql = """SELECT p.sample_id, p.contig, b.title, p.hamming_distance,
                    p.bitscore, p.evalue, p.identity, b.length, p.mismatch,
                    p.gaps, p.query_from, p.query_to, p.hit_from, p.hit_to,
                    p.align_len, p.qseq, p.hseq
             FROM {0} AS p
             LEFT JOIN staphopia_blastquery AS b
             ON p.query_id=b.id
             LEFT JOIN sample_basic AS s
             ON p.sample_id=s.sample_id
             WHERE p.sample_id IN ({1}) USER_PERMISSION
                   AND p.hamming_distance{2}0
             ORDER BY p.sample_id;""" .format(
        'sccmec_subtypes' if is_subtypes else 'sccmec_primers',
        ','.join([str(i) for i in sample_id]),
        '=' if exact_hits and not predict else '>='
    )

    if predict or hamming_distance:
        if is_subtypes:
            return predict_subtype_by_primers(
                sample_id,
                query_database(sql),
                hamming_distance=hamming_distance
            )
        else:
            return predict_type_by_primers(
                sample_id,
                query_database(sql),
                hamming_distance=hamming_distance
            )
    else:
        cols = ['sample_id', 'contig', 'title', 'hamming_distance', 'bitscore',
                'evalue', 'length', 'identity', 'mismatch', 'gaps',
                'query_from', 'query_to', 'hit_from', 'hit_to', 'align_len',
                'qseq', 'hseq']
        results = []
        for row in query_database(sql):
            result = OrderedDict()
            for col in cols:
                if col == 'title':
                    if '|' in row[col]:
                        result['target'], result['description'] = row[col].split('|')
                    else:
                        result['target'] = row[col]
                        result['description'] = row[col]
                else:
                    result[col] = row[col]
            results.append(result)

        return results


def get_sccmec_proteins_by_sample(sample_id, user_id):
    """Return SCCmec protein hits asscociated with a sample_id."""
    sql = """SELECT p.sample_id, p.contig, b.title, p.hamming_distance,
                    p.bitscore, p.evalue, b.length, p.identity,
                    p.mismatch, p.gaps, p.query_from, p.query_to,
                    p.hit_from, p.hit_to, p.align_len, p.qseq, p.hseq
             FROM sccmec_proteins AS p
             LEFT JOIN staphopia_blastquery AS b
             ON p.query_id=b.id
             LEFT JOIN sample_basic AS s
             ON p.sample_id=s.sample_id
             WHERE p.sample_id IN ({0}) USER_PERMISSION
             ORDER BY p.sample_id;""" .format(
        ','.join([str(i) for i in sample_id]),
        user_id,
    )

    cols = ['sample_id', 'contig', 'title', 'hamming_distance', 'bitscore',
            'evalue', 'length', 'identity', 'mismatch', 'gaps', 'query_from',
            'query_to', 'hit_from', 'hit_to', 'align_len', 'qseq', 'hseq']
    results = []
    for row in query_database(sql):
        result = OrderedDict()
        for col in cols:
            if col == 'title':
                result['target'], result['description'] = row[col].split('|')
            else:
                result[col] = row[col]
        results.append(result)


    return results


def get_sccmec_coverage_by_sample(sample_id, user_id):
    """Return SCCmec coverages asscociated with a sample_id."""
    sql = """SELECT cov.sample_id, cas.name as cassette, cov.total,
                    cov.minimum, cov.mean, cov.median, cov.maximum,
                    cov.meca_total, cov.meca_minimum, cov.meca_mean,
                    cov.meca_median, cov.meca_maximum
             FROM sccmec_coverage AS cov
             LEFT JOIN sccmec_cassette AS cas
             ON cov.cassette_id=cas.id
             LEFT JOIN sample_basic AS s
             ON cov.sample_id=s.sample_id
             WHERE cov.sample_id IN ({0}) USER_PERMISSION
             ORDER BY cov.sample_id ASC, cassette ASC;""".format(
        ','.join([str(i) for i in sample_id]),
        user_id
    )

    results = []
    for row in query_database(sql):
        if row['cassette'] not in ['IIb', 'IVd']:
            results.append(row)

    return results
