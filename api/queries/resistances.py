"""API utilities for resistance related viewsets."""
from collections import OrderedDict
from api.utils import query_database


def get_ariba_resistance(sample_id, user_id, mec_only=False):
    """Return resistance results associated with a sample."""
    cluster = {}
    sql = """SELECT * FROM resistance_cluster"""
    for row in query_database(sql):
        cluster[row['id']] = row

    sql = """SELECT r.sample_id, results
             FROM resistance_ariba AS r
             LEFT JOIN sample_basic AS s
             ON r.sample_id=s.sample_id
             WHERE r.sample_id IN ({0}) USER_PERMISSION
             ORDER BY r.sample_id ASC;""".format(
        ','.join([str(i) for i in sample_id])
    )

    results = []
    for row in query_database(sql):
        if row['results']:
            for i in row['results']:
                result = {}
                result['sample_id'] = row['sample_id']
                for key, val in i.items():
                    if key == 'cluster_id':
                        r_class = cluster[val]['resistance_class']
                        result['resistance_class'] = r_class
                        result['mechanism'] = cluster[val]['mechanism']
                        result['ref_name'] = cluster[val]['ref_name']
                        result['database'] = cluster[val]['database']
                        result['headers'] = cluster[val]['headers']
                    result[key] = val

                if mec_only:
                    if 'mec' in result['cluster'].lower() or 'pbp2' in result['cluster'].lower():
                        results.append(result)
                else:
                    results.append(result)
    return results


def get_ariba_resistance_report(sample_id, user_id, by_cluster=False,
                                include_all=False, mec_only=False):
    """Return resistance report based on class associated with a sample."""
    resistance_class = []
    omit = [
        'AAC3', 'APH3_PRIME_5', 'ARL-', 'ARLS', 'CLS', 'dha', 'FOLP_21',
        'GYRA_8', 'gyrB_1', 'MEPA_1', 'MEPR', 'MGRA', 'MPRF', 'NORA',
        'PARC_16', 'PARE+', 'PGSA', 'RLMH', 'RPOB+', 'RPOC', 'SAV1866',
        'TET38', 'TUFAB_10'
    ]
    if by_cluster:
        sql = """SELECT id, name, resistance_class
                 FROM resistance_cluster
                 ORDER BY name"""
        for row in query_database(sql):
            if row['name'] not in omit:
                if row['resistance_class']:
                    if mec_only:
                        if 'mec' in row['name'].lower() or 'pbp2' in row['name'].lower():
                            name = f"{row['name']};{row['resistance_class']}"
                            resistance_class.append(name)
                    else:
                        name = f"{row['name']};{row['resistance_class']}"
                        resistance_class.append(name)
    else:
        if mec_only:
            resistance_class.append('mec')
        else:
            sql = """SELECT id, name
                     FROM resistance_resistanceclass
                     ORDER BY name"""
            for row in query_database(sql):
                if row['name'] not in omit:
                    if row['name'].title() not in resistance_class:
                        if row['name'] == 'MLS':
                            resistance_class.append(row['name'])
                        elif row['name'] == 'betalactams':
                            resistance_class.append(row['name'].title())
                            resistance_class.append(f"{row['name'].title()} (mec)")
                        else:
                            resistance_class.append(row['name'].title())

    sql = """SELECT r.sample_id, summary
             FROM resistance_ariba AS r
             LEFT JOIN sample_basic AS s
             ON r.sample_id=s.sample_id
             WHERE r.sample_id IN ({0}) USER_PERMISSION
             ORDER BY r.sample_id ASC;""".format(
        ','.join([str(i) for i in sample_id])
    )

    results = []
    for row in query_database(sql):
        sample = OrderedDict()
        sample['sample_id'] = row['sample_id']
        for c in resistance_class:
            sample[c] = False

        for r in row['summary']:
            if r['cluster'] not in omit:
                if r['match'] == 'yes' or include_all:
                    if mec_only:
                        if 'mec' in r['cluster'].lower() or 'pbp2' in r['cluster'].lower():
                            if by_cluster:
                                name = f"{r['cluster']};{r['resistance_class']}"
                                sample[name] = True
                            else:
                                sample['mec'] = True
                    else:
                        if by_cluster:
                            name = f"{r['cluster']};{r['resistance_class']}"
                            sample[name] = True
                        else:
                            rclass = r['resistance_class']
                            if rclass == 'MLS':
                                sample[rclass] = True
                            elif rclass == 'betalactams':
                                sample[rclass.title()] = True
                                if 'mec' in r['cluster'].lower() or 'pbp2' in r['cluster'].lower():
                                    sample[f'{rclass.title()} (mec)'] = True
                            else:
                                sample[rclass.title()] = True

        results.append(sample)

    return results


def get_ariba_resistance_summary(sample_id, user_id, mec_only=False):
    """Return resistance summary based on class associated with a sample."""
    sql = """SELECT r.sample_id, summary
             FROM resistance_ariba AS r
             LEFT JOIN sample_basic AS s
             ON r.sample_id=s.sample_id
             WHERE r.sample_id IN ({0}) USER_PERMISSION
             ORDER BY r.sample_id ASC;""".format(
        ','.join([str(i) for i in sample_id])
    )

    results = []
    for row in query_database(sql):
        for r in row['summary']:
            sample = OrderedDict()
            sample['sample_id'] = row['sample_id']
            for key, val in r.items():
                sample[key] = val

            if mec_only:
                if 'mec' in sample['cluster'].lower() or 'pbp2' in sample['cluster'].lower():
                    results.append(sample)
            else:
                results.append(sample)

    return results
