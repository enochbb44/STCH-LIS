"""Seed the STCH LIS test database with realistic demo cases.

Creates 3 histology cases at each of the 11 workflow stages (33 cases),
each with a patient, referring doctor, workflow history timeline, and the
blocks / slides / results / dispatch data appropriate to its stage, plus
logbook entries synced the same way reception does.

Safe to re-run: previously seeded rows (clinical_history tagged
"[TEST DATA]") are deleted first; created staff/referring doctors are
reused.
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcs_project.settings')
import django
django.setup()

from datetime import timedelta
from django.utils import timezone
from accounts.models import User
from core.models import (
    Patient, ReferringDoctor, PathologyCase, WorkflowHistory,
    SpecimenBlock, Slide,
)
from core.name_utils import format_pathologist

STAGES = [
    ('RECEIVED', 'Received'),
    ('GROSSING', 'Grossing'),
    ('PROCESSING', 'Processing'),
    ('TISSUE_PROCESSING', 'Tissue Processing'),
    ('EMBEDDING', 'Embedding'),
    ('SECTIONING', 'Sectioning'),
    ('STAINING', 'Staining'),
    ('REPORTING', 'Reporting'),
    ('CONSULTANT_REVIEW', 'Consultant Review'),
    ('SIGNED_OUT', 'Signed Out'),
    ('RELEASED', 'Released'),
]
BASE_DAYS = [0, 1, 2, 3, 5, 6, 7, 9, 11, 13, 15]
MARKER = '[TEST DATA] '

# Benign clinical pictures for cases that have not reached reporting yet,
# so no cancer rule fires and they stay put in the workflow queues.
BENIGN_POOL = [
    ('Breast tissue', 'Right breast lump, FNAC site',
     'Lump noticed 3 months ago, slow growing, mobile, no axillary nodes.',
     'Fibroadenoma?'),
    ('Cervical biopsy', 'Cervix, 12 o\u2019clock',
     'Post-coital bleeding; colposcopy shows an acetowhite area.',
     'CIN 1?'),
    ('Colonic polyp', 'Sigmoid colon',
     'Routine screening colonoscopy found a 5 mm sessile polyp.',
     'Hyperplastic polyp?'),
    ('Skin lesion', 'Left forearm',
     'Pigmented lesion, stable; clinically a junctional naevus.',
     'Compound naevus?'),
    ('Gallbladder', 'Cholecystectomy specimen',
     'Recurrent right upper quadrant pain; ultrasound shows gallstones.',
     'Chronic cholecystitis'),
    ('Prostate chips', 'TURP chips',
     'Lower urinary tract symptoms; PSA 4.2, gland feels benign.',
     'Benign prostatic hyperplasia'),
    ('Thyroid nodule', 'Left thyroid lobe',
     'Solitary cold nodule on ultrasound; euthyroid.',
     'Colloid goitre?'),
    ('Endometrial biopsy', 'Endometrium',
     'Perimenopausal irregular bleeding; TVS otherwise normal.',
     'Proliferative endometrium?'),
    ('Appendix', 'Appendectomy specimen',
     'Right iliac fossa pain for 48 hours; ultrasound suggests appendicitis.',
     'Acute appendicitis'),
    ('Ovarian cyst', 'Right ovary, cystectomy',
     'Incidental simple cyst on ultrasound; CA-125 normal.',
     'Follicular cyst?'),
    ('Lymph node', 'Left cervical node excision',
     'Painless 2 cm node present for 6 weeks, not settling.',
     'Reactive hyperplasia?'),
]

# Definitive final diagnoses for REPORTING-stage onward.
REPORT_POOL = [
    ('Breast lumpectomy', 'Right breast, wide local excision',
     'Screen-detected mass; core biopsy showed high-grade DCIS.',
     'Invasive ductal carcinoma (NST), Nottingham grade 2; margins clear.',
     'Sections show invasive ductal carcinoma with associated high-grade DCIS. Tumour forms tubules in areas with intervening desmoplastic stroma. Excision margins are clear (closest 4 mm). Two sentinel nodes are free of tumour.'),
    ('Colonic resection', 'Right hemicolectomy',
     'Iron-deficiency anaemia; colonoscopy found a cecal mass.',
     'Moderately differentiated adenocarcinoma of the caecum (pT3 N0).',
     'Invasive adenocarcinoma forming glands and mucin pools, extending to pericolonic fat. 14 lymph nodes retrieved, all free of metastasis. Resection margins clear.'),
    ('Skin excision', 'Back, shave excision',
     'Slowly enlarging raised keratotic lesion.',
     'Basal cell carcinoma, nodular type; deep margins clear.',
     'Nodules of basaloid tumour cells with peripheral palisading and retraction artefact. No perineural or vascular invasion; deep margin clear.'),
    ('Thyroid lobectomy', 'Right thyroid lobe',
     '2.5 cm cold nodule; FNA reported suspicious.',
     'Papillary thyroid carcinoma, classic variant.',
     'Follicular cells with nuclear grooving, clearing and intranuclear inclusions forming papillae. No capsular or vascular invasion seen.'),
    ('Prostate biopsy', 'Prostate, 12 cores',
     'PSA 8.9; two cores felt suspicious on DRE.',
     'Prostatic adenocarcinoma, Gleason 3+4=7 in 2 of 12 cores.',
     'Adenocarcinoma involving 2 cores (10% and 15%). Gleason score 3+4=7 (grade group 2). No perineural invasion identified.'),
    ('Cervical cone', 'Cervix, LLETZ cone',
     'CIN 2 on previous punch biopsy.',
     'CIN 3; excision margins clear.',
     'Full-thickness squamous dysplasia with maturation towards the surface in places. Margins and deep endocervical margin are clear. No invasion.'),
    ('Lymph node excision', 'Left axillary node',
     'Enlarged node in a patient with known breast carcinoma.',
     'Reactive lymph node; no metastasis.',
     'Preserved nodal architecture with florid follicular and sinus hyperplasia. No carcinoma cells seen in the sections examined.'),
    ('Endometrial curettings', 'Endometrium',
     'Postmenopausal bleeding, 4 months.',
     'Endometrioid atypical hyperplasia.',
     'Crowded, back-to-back glands with cytological atypia but no stromal invasion. No malignant glands identified.'),
    ('Stomach biopsy', 'Gastric antrum',
     'Dyspepsia; gastroscopy shows a 8 mm antral ulcer.',
     'Chronic gastritis with intestinal metaplasia; H. pylori organisms present.',
     'Chronic inflammatory infiltrate with lymphoid follicles; gastric-type epithelium partially replaced by intestinal metaplasia. Curved bacilli consistent with H. pylori are present. No dysplasia or malignancy.'),
    ('Prostate biopsy', 'Prostate, 12 cores',
     'PSA 6.1; enlarged gland on ultrasound.',
     'Benign prostatic hyperplasia; no malignancy.',
     'Hyperplastic glands with corpora amylacea and foci of chronic prostatitis. No evidence of malignancy in all 12 cores, with good tissue preservation.'),
]

FIRST_NAMES = ['Abena', 'Kwabena', 'Akosua', 'Yaw', 'Ama', 'Kwame', 'Efua',
               'Kojo', 'Adjoa', 'Kofi', 'Abigail', 'Daniel', 'Mercy', 'Samuel',
               'Gifty', 'Emmanuel', 'Rita', 'Michael', 'Stella', 'Isaac',
               'Comfort', 'Joseph', 'Cynthia', 'Peter', 'Diana', 'Ebenezer',
               'Joyce', 'Matthew', 'Grace', 'Raymond', 'Serwaa', 'Theophilus',
               'Naomi']
LAST_NAMES = ['Mensah', 'Owusu', 'Boateng', 'Adjei', 'Asante', 'Darko',
              'Agyeman', 'Amankwah', 'Quartey', 'Bonsu', 'Osei', 'Tetteh',
              'Ankrah', 'Frimpong', 'Antwi', 'Sarpong']

DOCTORS = [
    ('Kwame', 'Owusu', 'STCH Medical Centre'),
    ('Yaa', 'Mensah', 'Accra Clinics'),
    ('Kofi', 'Adjei', 'Premier Medical Centre'),
    ('Abena', 'Boateng', 'St. Mary\u2019s Clinic'),
    ('Yaw', 'Agyeman', 'Valley View Clinic'),
    ('Akosua', 'Darko', 'Women\u2019s Health Centre'),
    ('Kojo', 'Asante', 'Ridgeview Hospital'),
    ('Efua', 'Amankwah', 'New Life Clinic'),
]
HOSPITALS = ['Saint Theresah Catholic Hospital', 'Korle Bu Teaching Hospital',
             'Premier Medical Centre', 'Valley View Clinic']


def _reset_number_sequences():
    """Rewind the per-prefix case-number counters for the current year.

    ``CaseNumberSequence`` never rewinds when rows are deleted, so re-running
    the seeder would otherwise keep inflating the next path number (e.g. the
    34th live case became ``PS/0088/26``).  Each counter is recomputed from the
    highest number still present, so with only demo rows the next number is 1.
    """
    import re
    from core.models import (
        CaseNumberSequence, PathologyCase, HistologyLog, CytologyLog,
        ResearchLog, AcademicResearchLog,
    )
    year = timezone.now().strftime('%y')
    sources = {
        'PS': [(PathologyCase, 'case_number'), (HistologyLog, 'path_number')],
        'PC': [(PathologyCase, 'case_number'), (CytologyLog, 'path_number')],
        'PR': [(ResearchLog, 'research_number'), (AcademicResearchLog, 'research_number')],
        'PM': [(PathologyCase, 'case_number')],
    }
    for prefix, pairs in sources.items():
        pattern = re.compile(rf'^{re.escape(prefix)}/(\d+)/{re.escape(year)}$')
        highest = 0
        for model, field in pairs:
            for value in model.objects.values_list(field, flat=True).iterator():
                match = pattern.match(str(value or ''))
                if match:
                    highest = max(highest, int(match.group(1)))
        CaseNumberSequence.objects.update_or_create(
            prefix=prefix, year=year, defaults={'next_val': highest + 1})
    print(f'reset number sequences for {year} (PS/PC/PR/PM -> 1)')


def main():
    admin = User.objects.filter(is_superuser=True).order_by('pk').first()
    if not admin:
        print('ERROR: no admin user found')
        return

    # --- staff users (reused across runs) --------------------------------
    def get_user(username, first, last, role):
        u = User.objects.filter(username=username).first()
        if not u:
            u = User(username=username, email=f'{username}@stch.local',
                     first_name=first, last_name=last, role=role,
                     is_active=True)
            u.set_password('Stch@1234!')
            u.save()
        return u

    pathologist = User.objects.filter(role='pathologist', is_active=True).order_by('pk').first()
    if not pathologist:
        pathologist = get_user('ralphadu', 'Raphael', 'Adu Brobbey', 'pathologist')
    else:
        # Sync stored name to the preferred spelling for reports and profile display.
        changed = False
        if pathologist.first_name == 'Ralphael' and pathologist.last_name == 'Adu Brobbey':
            pathologist.first_name = 'Raphael'
            changed = True
        if pathologist.first_name == 'Ralph' and pathologist.last_name == 'Adu':
            pathologist.first_name = 'Raphael'
            pathologist.last_name = 'Adu Brobbey'
            changed = True
        if changed:
            pathologist.save(update_fields=['first_name', 'last_name'])
    pathologist2 = get_user('asante', 'Ama', 'Asante', 'pathologist')
    technician = get_user('mensah', 'Emmanuel', 'Mensah', 'technician')
    lab_manager = get_user('owusu', 'Nana', 'Owusu', 'lab_manager')

    # --- wipe previous seeded demo cases ----------------------------------
    removed = PathologyCase.objects.filter(clinical_history__startswith=MARKER).count()
    PathologyCase.objects.filter(clinical_history__startswith=MARKER).delete()
    patient_cleanup = Patient.objects.filter(medical_record_number__startswith='MRN-DEMO-').count()
    Patient.objects.filter(medical_record_number__startswith='MRN-DEMO-').delete()
    print(f'removed {removed} previous demo cases (+ {patient_cleanup} demo patients)')

    # Rewind the case-number counters so numbering restarts at 1.
    _reset_number_sequences()

    # --- referring doctors -------------------------------------------------
    ref_docs = []
    for i, (fn, ln, hp) in enumerate(DOCTORS, 1):
        rd = ReferringDoctor.objects.filter(license_number=f'MD-D{100+i}').first()
        if not rd:
            rd = ReferringDoctor.objects.create(
                first_name=fn, last_name=ln, hospital_name=hp,
                license_number=f'MD-D{100+i}',
                phone=f'05 512 {3400+i:04d}', email=f'{ln.lower()}.{fn.lower()}@mail.example')
        ref_docs.append(rd)

    grossers = ['E. Mensah', 'M. Antwi', 'S. Ofosu']
    scientist = technician.get_full_name() or technician.username

    created_cases = 0
    for stage_idx, (stage_code, stage_label) in enumerate(STAGES):
        for idx in range(3):
            k = created_cases  # global running index
            fname = FIRST_NAMES[k % len(FIRST_NAMES)]
            lname = LAST_NAMES[(k * 3) % len(LAST_NAMES)]
            gender = 'F' if fname in ('Abena', 'Akosua', 'Ama', 'Efua', 'Adjoa',
                                      'Abigail', 'Mercy', 'Gifty', 'Rita',
                                      'Stella', 'Comfort', 'Cynthia', 'Diana',
                                      'Joyce', 'Grace', 'Serwaa', 'Naomi') else 'M'
            age = 22 + (k * 7) % 55
            patient, _ = Patient.objects.get_or_create(
                medical_record_number=f'MRN-DEMO-{1000 + k:04d}',
                defaults=dict(first_name=fname, last_name=lname, gender=gender,
                              age=age, phone=f'02 4{k%7} {500000 + k*13:06d}',
                              email=f'{fname}.{lname}@mail.example'),
            )

            if stage_idx < 7:
                sp, source, hist, diag = BENIGN_POOL[k % len(BENIGN_POOL)]
                final_diag = ''
                micro = ''
            else:
                sp, source, hist, final_diag, micro = REPORT_POOL[k % len(REPORT_POOL)]
                diag = final_diag

            # Received a few days ago depending on how far the case has moved.
            received = timezone.now() - timedelta(
                days=BASE_DAYS[stage_idx] + idx,
                hours=3 + (k % 5))
            rd = ref_docs[k % len(ref_docs)]
            case = PathologyCase(
                patient=patient,
                referring_doctor=rd,
                referring_clinician=f'Dr. {rd.first_name[:1]}. {rd.last_name}',
                hospital_name=HOSPITALS[k % len(HOSPITALS)],
                specimen_type=sp,
                specimen_source=source,
                clinical_history=MARKER + hist,
                clinical_diagnosis=diag,
                specimen_received_date=received,
                date_of_procedure=(received - timedelta(days=1)).date(),
                priority=('ROUTINE', 'URGENT', 'STAT')[idx % 3],
                case_type='HISTOLOGY',
                workflow_stage=stage_code,
            )
            case.save()  # assigns case_number

            # --- workflow history timeline -------------------------------
            def wh(stage, user, hours, note):
                wh_obj = WorkflowHistory.objects.create(
                    case=case, stage=stage, entered_by=user, notes=note)
                # entered_at is auto_now_add, so backdate it via update().
                WorkflowHistory.objects.filter(pk=wh_obj.pk).update(
                    entered_at=received + timedelta(hours=hours))

            wh('RECEIVED', admin, 0, 'Case accepted at reception')

            # The per-stage payload and additional history rows.
            if stage_idx >= 1:  # GROSSING and beyond
                n_blocks = 1 + k % 3
                case.gross_description = (
                    f'Specimen received in formalin, labelled "{case.case_number}". '
                    f'{n_blocks} cassette(s) submitted for processing. ')
                case.number_of_cassettes = n_blocks
                case.grossed_by = grossers[k % len(grossers)]
                case.save(update_fields=['gross_description', 'number_of_cassettes',
                                         'grossed_by', 'updated_at'])
                wh('GROSSING', technician, 20, 'Grossing complete')
                for b in range(n_blocks):
                    block = SpecimenBlock(case=case, tissue_type=sp,
                                          size='2.0 x 1.5 x 0.3 cm',
                                          grossed_by=case.grossed_by)
                    block.save()
            if stage_idx >= 2:  # PROCESSING and beyond
                case.scientist_name = scientist
                case.save(update_fields=['scientist_name', 'updated_at'])
                wh('PROCESSING', technician, 44, f'Processed by {scientist}')
            if stage_idx >= 3:
                wh('TISSUE_PROCESSING', technician, 68, 'Overnight tissue processing (18h cycle, paraffin)')
            if stage_idx >= 4:
                wh('EMBEDDING', technician, 92, 'Embedded in paraffin blocks')
            if stage_idx >= 5:  # SECTIONING and beyond
                wh('SECTIONING', technician, 116, 'Sections cut at 4 µm')
                for block in case.blocks.all():
                    for _ in range(1 + k % 2):
                        Slide(block=block, stain_type='',
                              prepared_by=scientist).save()
            if stage_idx >= 6:  # STAINING and beyond
                case.stain_type = 'H&E'
                case.number_of_slides = Slide.objects.filter(block__case=case).count()
                case.save(update_fields=['stain_type', 'number_of_slides', 'updated_at'])
                wh('STAINING', technician, 140, 'H&E staining completed')
                for slide in Slide.objects.filter(block__case=case):
                    slide.stain_type = 'H&E'
                    slide.save(update_fields=['stain_type'])

            if stage_idx >= 7:  # REPORTING and beyond
                case.microscopic_description = micro
                case.final_diagnosis = final_diag
                case.pathologist_name = format_pathologist(pathologist.get_full_name() or pathologist.username)
                case.assigned_pathologist = pathologist
                case.is_reported = True
                case.report_date = received + timedelta(days=max(7, BASE_DAYS[stage_idx]), hours=2)
                case.save()
                wh('REPORTING', pathologist, 160, f'Reported by {case.pathologist_name}')
            if stage_idx >= 8:  # CONSULTANT_REVIEW and beyond
                case.consultant_name = format_pathologist(pathologist2.get_full_name() or pathologist2.username)
                case.review_notes = 'Diagnosis and grading confirmed on internal review.'
                case.save(update_fields=['consultant_name', 'review_notes', 'updated_at'])
                wh('CONSULTANT_REVIEW', pathologist2, 184,
                   'Consultant review complete')
            if stage_idx >= 9:  # SIGNED_OUT
                case.is_reviewed = True
                case.save(update_fields=['is_reviewed', 'updated_at'])
                wh('SIGNED_OUT', pathologist2, 208, 'Report signed out')
            if stage_idx >= 10:  # RELEASED
                case.dispatched_at = received + timedelta(days=BASE_DAYS[10], hours=3)
                case.dispatch_method = 'Email'
                case.dispatch_destination = f'{fname}.{lname}@mail.example'
                case.dispatch_contact = case.referring_clinician
                case.dispatch_remarks = 'Report emailed to requesting clinician.'
                case.dispatch_status = 'DISPATCHED'
                case.save(update_fields=['dispatched_at', 'dispatch_method',
                                         'dispatch_destination', 'dispatch_contact',
                                         'dispatch_remarks', 'dispatch_status',
                                         'updated_at'])
                wh('RELEASED', admin, 232, 'Report dispatched by email')

            # Mirror to the histology logbook as reception does.
            try:
                _sync_case_logs(case, admin)
            except Exception as exc:
                print(f'  ! log sync failed for {case.case_number}: {exc}')

            created_cases += 1

    # --- summary -----------------------------------------------------------
    from collections import Counter
    counts = Counter(
        PathologyCase.objects.values_list('workflow_stage', flat=True))
    print(f'created {created_cases} demo cases:')
    for code, label in STAGES:
        print(f'  {label:20} {counts.get(code, 0)}')


if __name__ == '__main__':
    main()