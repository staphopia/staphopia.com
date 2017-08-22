CREATE OR REPLACE VIEW sample_summary_view AS
SELECT
    -- Sample
    s.id,
    s.id AS sample_id,
    s.is_paired,
    s.is_public,
    s.is_published,
    s.sample_tag,
    s.document,
    u.username,
    m.contains_ena_metadata,
    m.study_accession,
    m.study_title,
    m.study_alias,
    m.secondary_study_accession,
    m.sample_accession,
    m.secondary_sample_accession,
    m.submission_accession,
    m.experiment_accession,
    m.experiment_title,
    m.experiment_alias,
    m.tax_id,
    m.scientific_name,
    m.instrument_platform,
    m.instrument_model,
    m.library_layout,
    m.library_strategy,
    m.library_selection,
    m.center_name,
    m.center_link,
    m.cell_line,
    m.collected_by,
    m.location,
    m.country,
    m.region,
    m.coordinates,
    m.description,
    m.environmental_sample,
    m.biosample_first_public,
    m.germline,
    m.isolate,
    m.isolation_source,
    m.serotype,
    m.serovar,
    m.sex,
    m.submitted_sex,
    m.strain,
    m.sub_species,
    m.tissue_type,
    m.biosample_scientific_name,
    m.sample_alias,
    m.checklist,
    m.biosample_center_name,
    m.environment_biome,
    m.environment_feature,
    m.environment_material,
    m.project_name,
    m.host,
    m.host_status,
    m.host_sex,
    m.submitted_host_sex,
    m.host_body_site,
    m.investigation_type,
    m.sequencing_method,
    m.broker_name,

    -- FASTQ
    CASE fq.rank WHEN 3 THEN 'Gold' WHEN 2 THEN 'Silver' ELSE 'Bronze' END as rank,
    fq.total_bp,
    fq.read_total,
    fq.coverage,
    fq.read_min,
    fq.read_mean,
    fq.read_median,
    fq.read_std,
    fq.read_max,
    fq.read_25th,
    fq.read_75th,

    CASE WHEN fq.qual_mean > 41 THEN (fq.qual_mean - 31) ELSE fq.qual_mean END as q_score,
    fq.qual_mean,
    fq.qual_std,
    fq.qual_25th,
    fq.qual_median,
    fq.qual_75th,

    -- Assembly
    assembly.total_contig,
    assembly.total_contig_length,
    assembly.min_contig_length,
    assembly.median_contig_length,
    assembly.mean_contig_length,
    assembly.max_contig_length,
    assembly.n50_contig_length,
    assembly.l50_contig_count,
    assembly.ng50_contig_length,
    assembly.lg50_contig_count,
    assembly.contigs_greater_1k,
    assembly.contigs_greater_10k,
    assembly.contigs_greater_100k,
    assembly.contigs_greater_1m,
    assembly.percent_contigs_greater_1k,
    assembly.percent_contigs_greater_10k,
    assembly.percent_contigs_greater_100k,
    assembly.percent_contigs_greater_1m,
    assembly.contig_percent_a,
    assembly.contig_percent_t,
    assembly.contig_percent_g,
    assembly.contig_percent_c,
    assembly.contig_percent_n,
    assembly.contig_non_acgtn,
    assembly.num_contig_non_acgtn,
    (assembly.contig_percent_g + assembly.contig_percent_c) AS gc_content,

    -- Variants
    variant.snp AS total_snps,
    variant.indel AS total_indels,

    -- MLST
    'ST'||mlst.st_original as st_original,
    'ST'||mlst.st_stripped as st_stripped,
    mlst.is_exact

FROM sample_sample AS s
LEFT JOIN assembly_stats AS assembly ON s.id=assembly.sample_id AND assembly.is_scaffolds is FALSE AND assembly.is_plasmids is FALSE
LEFT JOIN sequence_stat AS fq ON s.id=fq.sample_id AND fq.is_original is FALSE
LEFT JOIN auth_user AS u ON s.user_id=u.id
LEFT JOIN sample_metadata AS m ON s.id=m.sample_id
LEFT JOIN mlst_srst2 AS mlst ON s.id=mlst.sample_id
LEFT JOIN variant_counts as variant ON s.id=variant.sample_id
ORDER BY s.id DESC;

CREATE TABLE sample_summary
AS SELECT * FROM sample_summary_view;
