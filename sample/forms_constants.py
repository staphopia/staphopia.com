'''
    Use this constant values to be used in forms.py and models.py
'''
from django import forms
from django.utils.translation import ugettext_lazy as _

MAX_FILE_SIZE = 2147483648 # 2 GB

ACCEPTED_FILETYPES = [
    'application/x-bzip2',
    'application/x-bzip',
    'application/x-gzip',
]

SUBMISSION_FIELDS = [
    # Project Information
    'contact_name', 'contact_email', 'contact_link', 'sequencing_center',
    'sequencing_center_link', 'sequencing_date', 'sequencing_libaray_method',
    'sequencing_platform',

    # Publication Inforamtion
    'publication_link', 'pubmed_id', 'doi', 'funding_agency', 
    'funding_agency_link',
    
    # Organism Information
    'strain', 'isolation_date', 'isolation_country', 'isolation_city',
    'isolation_region', 'host_name', 'host_health', 'host_age', 'host_gender',
    'comments',
                             
    # Phenotype Information
    'vancomycin_mic', 'penicillin_mic', 'oxacillin_mic', 'clindamycin_mic',
    'daptomycin_mic', 'levofloxacin_mic', 'linezolid_mic', 'rifampin_mic',
    'tetracycline_mic', 'trimethoprim_mic', 'source',
    
    # Sequence Information
    'is_public', 'is_paired',
]

SUBMISSION_LABELS = {
    # Project Information
    'contact_name':_('Contact Name'),
    'contact_email':_('Contact Email'),
    'contact_link':_('Contact Link'),
    'sequencing_center':_('Sequencing Center'),
    'sequencing_center_link':_('Sequencing Center Link'),
    'sequencing_date':_('Sequencing Date'),
    'sequencing_libaray_method':_('Sequencing Library Method'),
    'sequencing_platform':_('Sequencing Platform'),

    # Publication Inforamtion
    'publication_link':_('Publication Link'),
    'pubmed_id':_('PubMed ID'),
    'doi':_('Digital Object Identifier (DOI)'),
    'funding_agency':_('Funding Agency'),
    'funding_agency_link':_('Funding Agency Link'),
    
    # Organism Information
    'strain':_('Strain'),
    'isolation_date':_('Isolation Date'),
    'isolation_country':_('Isolation Country'),
    'isolation_city':_('Isolation City'),
    'isolation_region':_('Isolation Region'),
    'host_name':_('Host Species Name'), # Should have taxon id
    'host_health':_('Host Health'),
    'host_age':_('Host Age'),
    'host_gender':_('Host Gender'),
    'comments':_('Comments'),
                             
    # Phenotype Information
    'vancomycin_mic':_('Vancomyocin'),
    'penicillin_mic':_('Penicillin'),
    'oxacillin_mic':_('Oxacillin'),
    'clindamycin_mic':_('Clindamycin'),
    'daptomycin_mic':_('Daptomycin'),
    'levofloxacin_mic':_('Levofloxacin'),
    'linezolid_mic':_('Linezolid'),
    'rifampin_mic':_('Rifampin'),
    'tetracycline_mic':_('Tetracycline'),
    'trimethoprim_mic':_('Trimethoprim-Sulfamethoxazole'),
    'source':_('Source'),
    
    # Sequence Information
    'is_public':_('Make Genome Public'),
    'is_paired':_('Reads are paired'),
    'sequence_file':_('Compressed (bzip2, gzip) FASTQ File'),

}

SUBMISSION_WIDGETS = {
    # Project Information
    'contact_name': forms.TextInput(attrs={
            'placeholder': 'Alexander Ogston',
            'value': ''
        }),
    'contact_email': forms.TextInput(attrs={
            'placeholder': 'usa300@staphopia.com'
        }),
    'contact_link': forms.TextInput(attrs={
            'placeholder': 'www.staphopia.com/contact/'
        }),
    'sequencing_center': forms.TextInput(attrs={
            'placeholder': 'Emory Integrated Genomics Core'
        }),
    'sequencing_center_link': forms.TextInput(attrs={
            'placeholder': 'eigc.emory.edu'
        }),
    'sequencing_date': forms.TextInput(attrs={'placeholder':  '03/11/2001'}),
    'sequencing_libaray_method': forms.TextInput(attrs={
            'placeholder': 'Standard MinION protocol'
        }),

    # Publication Inforamtion
    'publication_link': forms.TextInput(attrs={
            'placeholder': 'www.ncbi.nlm.nih.gov/pmc/articles/PMC1427395/'
        }),
    'pubmed_id': forms.TextInput(attrs={'placeholder':  '17860813'}),
    'doi': forms.TextInput(attrs={'placeholder':  '10.1128/JB.00951-10'}),
    'funding_agency': forms.TextInput(attrs={'placeholder':  'NIH'}),
    'funding_agency_link': forms.TextInput(attrs={
            'placeholder': 'www.nih.gov'
        }),
    
    # Organism Information
    'strain': forms.TextInput(attrs={'placeholder':  'USA300'}),
    'isolation_date': forms.TextInput(attrs={'placeholder':  '6/7/2014'}),
    'isolation_country': forms.TextInput(attrs={
            'placeholder': 'United States'
        }),
    'isolation_city': forms.TextInput(attrs={'placeholder':  'Atlanta'}),
    'isolation_region': forms.TextInput(attrs={'placeholder':  'Georgia'}),
    'host_name': forms.TextInput(attrs={'placeholder':  'Homo sapiens'}),
    'host_age': forms.TextInput(attrs={'placeholder':  '50'}),
    'comments': forms.Textarea(attrs={
            'placeholder': ('Any comments about this sample you may have. '
                           '(i.e. Patient acquired pathogen from sibling.)')
        }),
}

FIELDS = {
    # Project Information
    'contact_name':['Contact Name', 'Alexander Ogston'],
    'contact_email':['Contact Email', 'usa300@staphopia.com'],
    'contact_link':['Contact Link', 'www.staphopia.com/contact/'],
    'sequencing_center':['Sequencing Center',  'Emory Integrated Genomics Core'],
    'sequencing_center_link':['Sequencing Center Link', 'eigc.emory.edu'],
    'sequencing_date':['Sequencing Date', '03/11/2001'],
    'sequencing_libaray_method':['Sequencing Library Method',  'Standard MinION protocol'],
    'sequencing_platform':['Sequencing Platform', ''],

    # Publication Inforamtion
    'publication_link':['Publication Link', 'www.ncbi.nlm.nih.gov/pmc/articles/PMC1427395/'],
    'pubmed_id':['PubMed ID', '17860813'],
    'doi':['Digital Object Identifier (DOI)', '10.1128/JB.00951-10'],
    'funding_agency':['Funding Agency', 'NIH'],
    'funding_agency_link':['Funding Agency Link', 'www.nih.gov'],
    
    # Organism Information
    'strain':['Strain', 'USA300'],
    'isolation_date':['Isolation Date', '6/7/2014'],
    'isolation_country':['Isolation Country', 'United States'],
    'isolation_city':['Isolation City', 'Atlanta'],
    'isolation_region':['Isolation Region', 'Georgia'],
    'host_name':['Host Species Name', 'Homo sapiens'], # Should have taxon id
    'host_health':['Host Health','Select'],
    'host_age':['Host Age', '50'],
    'host_gender':['Host Gender', 'Male, Female, unknown'],
    'comments':['Comments', ('Any comments about this sample you may have. '
                             '(i.e. Patient acquired pathogen from sibling.)')],
                             
    # Phenotype Information
    'vancomycin_mic':['Vancomyocin',''],
    'penicillin_mic':['Penicillin',''],
    'oxacillin_mic':['Oxacillin', ''],
    'clindamycin_mic':['Clindamycin', ''],
    'daptomycin_mic':['Daptomycin', ''],
    'levofloxacin_mic':['Levofloxacin', ''],
    'linezolid_mic':['Linezolid', ''],
    'rifampin_mic':['Rifampin', ''],
    'tetracycline_mic':['Tetracycline', ''],
    'trimethoprim_mic':['Trimethoprim-Sulfamethoxazole', ''],
    'source':['Source', ''],
    
    # Sequence Information
    'is_public':['Make Genome Public', ''],
    'is_paired':['Reads are paired', ''],
    'sequence_file':['Compressed (bzip2, gzip, zip) FASTQ File',''],

}

REQUIRED_FIELDS = [
    'contact_name',
    'contact_email',
    'sequencing_center',
    'sequencing_platform',
    'sequence_file',
]

POST_IGNORE = [
    'submit', 
    'csrfmiddlewaretoken',
    'is_public',
    'sequence_file',
]


SELECT_FIELDS = [
    'sequencing_platform',
    'host_health',
    'source',
    'host_gender',
]


FIELD_ORDER = [
    #Project Information
    'contact_name',
    'contact_email',
    'contact_link',
    'sequencing_center',
    'sequencing_center_link',
    'sequencing_date',
    'sequencing_libaray_method',
    'sequencing_platform',
    
    #Publication Information
    'publication_link',
    'pubmed_id',
    'doi',
    'funding_agency',
    'funding_agency_link',

    #Organism Information
    'strain',
    'isolation_date',
    'isolation_country',
    'isolation_city',
    'isolation_region',
    'host_name',
    'host_health',
    'host_age',
    'host_gender',
    'comments',

    #Phenotype Information  
    'vancomycin_mic',
    'penicillin_mic',
    'oxacillin_mic',
    'clindamycin_mic',
    'daptomycin_mic',
    'levofloxacin_mic',
    'linezolid_mic',
    'rifampin_mic',
    'tetracycline_mic',
    'trimethoprim_mic',
    'source',  

    # Sequence Information
    'is_public',
    'is_paired',
    'sequence_file',
]

CHOICES = {
    'sequencing_platform':(
        ('', 'Select One'),
        ('454 GS Junior', '454 GS Junior'),
        ('Illumina MiSeq', 'Illumina MiSeq'),
        ('Illumina HiSeq 2000', 'Illumina HiSeq 2000'),
        ('Illumina HiSeq 2500', 'Illumina HiSeq 2500'),
        ('Ion Torrent PGM', 'Ion Torrent PGM'),
        ('PacBio RS', 'PacBio RS'),
        ('', '--------------------'),
        ('454 GS 20', '454 GS 20'),
        ('454 GS FLX', '454 GS FLX'),
        ('454 GS FLX Titanium', '454 GS FLX Titanium'),
        ('454 GS FLX+', '454 GS FLX+'),
        ('Illumina Genome Analyzer', 'Illumina Genome Analyzer'),
        ('Illumina Genome Analyzer II', 'Illumina Genome Analyzer II'),
        ('Illumina Genome Analyzer IIx', 'Illumina Genome Analyzer IIx'),
        ('Illumina HiScanSQ', 'Illumina HiScanSQ'),
        ('Illumina HiSeq 1000', 'Illumina HiSeq 1000'),
        ('Illumina HiSeq 1500', 'Illumina HiSeq 1500'),
        ('Ion Torrent Proton', 'Ion Torrent Proton'),
        ('AB 310 Genetic Analyzer', 'AB 310 Genetic Analyzer'),
        ('AB 3130 Genetic Analyzer', 'AB 3130 Genetic Analyzer'),
        ('AB 3130xL Genetic Analyzer', 'AB 3130xL Genetic Analyzer'),
        ('AB 3500 Genetic Analyzer', 'AB 3500 Genetic Analyzer'),
        ('AB 3500xL Genetic Analyzer', 'AB 3500xL Genetic Analyzer'),
        ('AB 3730 Genetic Analyzer', 'AB 3730 Genetic Analyzer'),
        ('AB 3730xL Genetic Analyzer', 'AB 3730xL Genetic Analyzer'),
        ('AB 5500 Genetic Analyzer', 'AB 5500 Genetic Analyzer'),
        ('AB 5500xl Genetic Analyzer', 'AB 5500xl Genetic Analyzer'),
        ('AB SOLiD 3 Plus System', 'AB SOLiD 3 Plus System'),
        ('AB SOLiD 4 System', 'AB SOLiD 4 System'),
        ('AB SOLiD 4hq System', 'AB SOLiD 4hq System'),
        ('AB SOLiD PI System', 'AB SOLiD PI System'),
        ('AB SOLiD System 1.0', 'AB SOLiD System 1.0'),
        ('AB SOLiD System 2.0', 'AB SOLiD System 2.0'),
        ('AB SOLiD System 3.0', 'AB SOLiD System 3.0'),
        ('Complete Genomics', 'Complete Genomics'),
        ('Helicos HeliScope', 'Helicos HeliScope'),
    ),
    
    'host_health':(
        ('', 'Select One'),
        ('Acute Infective Endocarditis', 'Acute Infective Endocarditis'),
        ('Boils', 'Boils'),
        ('Bacteremia', 'Bacteremia'),
        ('Carbuncles', 'Carbuncles'),
        ('Cellulitis', 'Cellulitis'),
        ('Food Poisoning', 'Food Poisoning'),
        ('Gastroenteritis', 'Gastroenteritis'),
        ('Impetigo', 'Impetigo'),
        ('Necrotizing pneumonia', 'Necrotizing pneumonia'),
        ('Osteomyelitis', 'Osteomyelitis'),
        ('Pneumonia', 'Pneumonia'),
        ('Septic arthritis', 'Septic arthritis'),
        ('Septicemia', 'Septicemia'),
        ('Staphylococcal Scalded Skin Syndrome', 'Staphylococcal Scalded Skin Syndrome'),
        ('Toxic Shock Syndrome', 'Toxic Shock Syndrome'),
        ('Other', 'Other'),
    ),
    
    'host_gender':(
        ('', 'Select One'),
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Not Specified', 'Not Specified'),
    ),

    'source':(
        ('', 'Select One'),
        ('Blood', 'Blood'),
        ('Body Fluid', 'Body Fluid'),
        ('Respiratory', 'Respiratory'),
        ('Tissue', 'Tissue'),
        ('Urine', 'Urine'),
        ('Wound', 'Wound'),
        ('Not Specified', 'Not Specified'),
        ('', '--------------------'),
        ('Biopsy NOS', 'Biopsy NOS'),
        ('Blood for Respiratory', 'Blood for Respiratory'),
        ('Body Fluid NOS', 'Body Fluid NOS'),
        ('Cerebrospinal Fluid', 'Cerebrospinal Fluid'),
        ('Colonic Wash', 'Colonic Wash'),
        ('Conjunctiva', 'Conjunctiva'),
        ('Contact Lens', 'Contact Lens'),
        ('Cord Blood', 'Cord Blood'),
        ('Cornea', 'Cornea'),
        ('Cornea Donor Rim', 'Cornea Donor Rim'),
        ('Cryoprecipitate Product', 'Cryoprecipitate Product'),
        ('Cyst Fluid', 'Cyst Fluid'),
        ('Decubitus Ulcer', 'Decubitus Ulcer'),
        ('Drainage', 'Drainage'),
        ('Drainage NOS', 'Drainage NOS'),
        ('Duodenal Drainage', 'Duodenal Drainage'),
        ('Ear', 'Ear'),
        ('Endocervix', 'Endocervix'),
        ('Endotracheal Aspirate', 'Endotracheal Aspirate'),
        ('Environmental', 'Environmental'),
        ('Esophageal Brush', 'Esophageal Brush'),
        ('Eye', 'Eye'),
        ('Eyelid ', 'Eyelid '),
        ('Fecal Aspirate', 'Fecal Aspirate'),
        ('Feces', 'Feces'),
        ('Fine Needle Aspirate', 'Fine Needle Aspirate'),
        ('Fistula', 'Fistula'),
        ('Gastric Fluid', 'Gastric Fluid'),
        ('Graft', 'Graft'),
        ('Groin', 'Groin'),
        ('Hair', 'Hair'),
        ('Heart Valve', 'Heart Valve'),
        ('Heart Valve - Porcine', 'Heart Valve - Porcine'),
        ('Hepatobiliary Brushing', 'Hepatobiliary Brushing'),
        ('Human Progenitor Cells-Apheresis', 'Human Progenitor Cells-Apheresis'),
        ('Human Progenitor Cells-Cord', 'Human Progenitor Cells-Cord'),
        ('Human Progenitor Cells-Marrow', 'Human Progenitor Cells-Marrow'),
        ('Implanted Material', 'Implanted Material'),
        ('Incision', 'Incision'),
        ('Intrauterine Device', 'Intrauterine Device'),
        ('Introducer Sheath', 'Introducer Sheath'),
        ('Islet Cells', 'Islet Cells'),
        ('Jackson Pratt Drainage', 'Jackson Pratt Drainage'),
        ('Joint Fluid', 'Joint Fluid'),
        ('Lesion', 'Lesion'),
        ('Liver Biopsy', 'Liver Biopsy'),
        ('Lochia', 'Lochia'),
        ('Lung Aspirate', 'Lung Aspirate'),
        ('Lymph Node', 'Lymph Node'),
        ('Middle Ear Fluid', 'Middle Ear Fluid'),
        ('Mini Bronchoalveolar Lavage', 'Mini Bronchoalveolar Lavage'),
        ('Nail', 'Nail'),
        ('Nares', 'Nares'),
        ('Nasal Wash', 'Nasal Wash'),
        ('Nasopharyngeal', 'Nasopharyngeal'),
        ('Other Blood Bank Product', 'Other Blood Bank Product'),
        ('Pancreas Fluid', 'Pancreas Fluid'),
        ('Pelvic Fluid', 'Pelvic Fluid'),
        ('Penile Discharge', 'Penile Discharge'),
        ('Penis', 'Penis'),
        ('Penrose Drain', 'Penrose Drain'),
        ('Pericardial Fluid', 'Pericardial Fluid'),
        ('Perirectum', 'Perirectum'),
        ('Peritoneal Dialysis Fluid', 'Peritoneal Dialysis Fluid'),
        ('Peritoneal Fluid', 'Peritoneal Fluid'),
        ('Pharmacy', 'Pharmacy'),
        ('Pharmacy Cardioplegic Fluid', 'Pharmacy Cardioplegic Fluid'),
        ('PICC Line', 'PICC Line'),
        ('Pilonidal Cyst', 'Pilonidal Cyst'),
        ('Pinworm Preparation', 'Pinworm Preparation'),
        ('Plasma', 'Plasma'),
        ('Plasma Product', 'Plasma Product'),
        ('Platelet Product', 'Platelet Product'),
        ('Pleural Fluid', 'Pleural Fluid'),
        ('Products of Conception', 'Products of Conception'),
        ('Pustule', 'Pustule'),
        ('QC', 'QC'),
        ('Rectum', 'Rectum'),
        ('Red Blood Cell Product', 'Red Blood Cell Product'),
        ('Retroperitoneal', 'Retroperitoneal'),
        ('Semen', 'Semen'),
        ('Serum', 'Serum'),
        ('Sinus', 'Sinus'),
        ('Skin', 'Skin'),
        ('Spore Strip', 'Spore Strip'),
        ('Sputum', 'Sputum'),
        ('Sputum Induced', 'Sputum Induced'),
        ('Stem Cells NOS', 'Stem Cells NOS'),
        ('Suprapubic Bladder Aspirate', 'Suprapubic Bladder Aspirate'),
        ('Swan Ganz Catheter', 'Swan Ganz Catheter'),
        ('Synovial Fluid', 'Synovial Fluid'),
        ('Throat', 'Throat'),
        ('Tissue NOS', 'Tissue NOS'),
        ('Tracheostomy Site', 'Tracheostomy Site'),
        ('Triple Lumen Catheter Tip', 'Triple Lumen Catheter Tip'),
        ('Umbilicus', 'Umbilicus'),
        ('Urethra', 'Urethra'),
        ('Urine Cystoscopic', 'Urine Cystoscopic'),
        ('Urine Nephrostomy', 'Urine Nephrostomy'),
        ('Urine, Catherized', 'Urine, Catherized'),
        ('Urine, Clean Catch', 'Urine, Clean Catch'),
        ('Urine, Ileal Conduit', 'Urine, Ileal Conduit'),
        ('Uvula', 'Uvula'),
        ('Vaginal', 'Vaginal'),
        ('Vaginal-Rectal', 'Vaginal-Rectal'),
        ('Ventricular Fluid CSF', 'Ventricular Fluid CSF'),
        ('Vertebra', 'Vertebra'),
        ('Vesicle', 'Vesicle'),
        ('Vitreous Fluid', 'Vitreous Fluid'),
        ('Vulva', 'Vulva'),
        ('Water', 'Water'),
        ('Whole Blood', 'Whole Blood'),
    ),
}