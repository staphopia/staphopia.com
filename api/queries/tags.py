"""API utilities for sample related viewsets."""
from api.utils import query_database


def get_samples_by_tag(tag, is_id=True):
    """Return samples associated with a tag."""
    sql = """SELECT s.sample_id, s.name, s.is_public, s.is_published, s.st,
                    s.rank
             FROM tag_tosample AS t
             LEFT JOIN sample_basic AS s
             ON t.sample_id=s.sample_id
             LEFT JOIN tag_tag AS n
             ON t.tag_id=n.id
             WHERE {0}
             ORDER BY s.name ASC;""".format(
        f"t.tag_id={tag}" if is_id else f"n.tag='{tag}'"
    )
    return query_database(sql)


def get_tags_by_sample(sample_id, user_id):
    """Return tags associated with a sample."""
    sql = """SELECT s.sample_id, s.tag_id, t.tag, t.comment
             FROM tag_tosample AS s
             LEFT JOIN tag_tag AS t
             ON s.tag_id=t.id
             LEFT JOIN sample_sample AS a
             ON s.sample_id=a.id
             WHERE s.sample_id={0}
                   AND (a.is_public=TRUE OR a.user_id={1});""".format(
        sample_id,
        user_id
    )
    return query_database(sql)


def get_all_tags(tag=None):
    """Return tags associated with a user."""
    tag_sql = ""
    if tag:
        tag_sql = f"AND tag='{tag}'"

    sql = """SELECT t.id as tag_id, tag, comment
             FROM tag_tag as t
             LEFT JOIN auth_user as u
             ON (u.id=t.user_id OR u.username='ena') {0}
             WHERE u.username='ena' {0};""".format(tag_sql)

    return query_database(sql)


def get_user_tags(user_id, tag=None):
    """Return tags associated with a user."""
    tag_sql = ""
    if tag:
        tag_sql = f"AND tag='{tag}'"
    sql = """SELECT id as tag_id, tag, comment
             FROM tag_tag
             WHERE user_id={0} {1};""".format(user_id, tag_sql)

    return query_database(sql)


def get_public_tags(tag=None):
    """Return tags associated with a user."""
    tag_sql = ""
    if tag:
        tag_sql = f"AND tag='{tag}'"
    sql = """SELECT t.id as tag_id, tag, comment
             FROM tag_tag as t
             LEFT JOIN auth_user as u
             ON u.id=t.user_id
             WHERE u.username='ena' {0};""".format(tag_sql)

    return query_database(sql)
