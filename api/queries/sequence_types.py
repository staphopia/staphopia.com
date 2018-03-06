"""API utilities for MLST related viewsets."""
from collections import OrderedDict
from api.utils import query_database, get_sample_permisions


def get_unique_st_samples():
    """Return list of public ENA samples with a unique ST."""
    return query_database('SELECT * FROM unique_mlst_samples;')


def get_sequence_type(sample_id, user):
    """Return MLST loci results associated with a sample."""
    sql = """SELECT sample_id, st, ariba, mentalist, blast
             FROM mlst_mlst AS m
             LEFT JOIN sample_sample AS s
             ON m.sample_id=s.id
             WHERE m.sample_id IN ({0}) AND ({1})
             ORDER BY m.sample_id ASC;""".format(
        ','.join([str(i) for i in sample_id]),
        get_sample_permisions(user)
    )

    return query_database(sql)

def get_cgmlst(sample_id, user):
    """Return cgMLST loci results associated with a sample."""
    sql = "SELECT id, name FROM cgmlst_loci;"
    loci = {}
    for row in query_database(sql):
        loci[str(row['id'])] = row['name']

    sql = """SELECT sample_id, mentalist
             FROM cgmlst_cgmlst AS m
             LEFT JOIN sample_sample AS s
             ON m.sample_id=s.id
             WHERE m.sample_id IN ({0}) AND ({1})
             ORDER BY m.sample_id ASC;""".format(
        ','.join([str(i) for i in sample_id]),
        get_sample_permisions(user)
    )
    results = []
    for row in query_database(sql):
        cgmlst = OrderedDict()
        cgmlst['sample_id'] = row['sample_id']
        for k in sorted(row['mentalist'], key=lambda x: int(x)):
            # k = Loci, v = Allele
            cgmlst[loci[k]] = row['mentalist'][k]
        results.append(cgmlst)
    return results
