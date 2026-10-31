# PCS LIS — Complete User Guide

**Pathology Consultancy Services — Laboratory Information System**
Version 2.0

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Getting Started](#2-getting-started)
3. [Dashboard](#3-dashboard)
4. [Case Reception](#4-case-reception)
5. [Grossing](#5-grossing)
6. [Processing](#6-processing)
7. [Reporting](#7-reporting)
8. [Consultant Review](#8-consultant-review)
9. [Dispatch & Sent Reports](#9-dispatch--sent-reports)
10. [Logbooks](#10-logbooks)
11. [Cancer Registry](#11-cancer-registry)
12. [Immunohistochemistry (IHC)](#12-immunohistochemistry-ihc)
13. [Synoptic Reporting](#13-synoptic-reporting)
14. [Slide Scanning & Digital Pathology](#14-slide-scanning--digital-pathology)
15. [Billing & Invoicing](#15-billing--invoicing)
16. [Facility Portal](#16-facility-portal)
17. [Administration](#17-administration)
18. [AI Assistant — Friday](#18-ai-assistant--friday)
19. [Archiving](#19-archiving)
20. [User Profile & Security](#20-user-profile--security)
21. [Keyboard Shortcuts & Tips](#21-keyboard-shortcuts--tips)
22. [Troubleshooting](#22-troubleshooting)

---

## 1. System Overview

### What is PCS LIS?

PCS LIS is a comprehensive Laboratory Information System designed for pathology laboratories. It manages the entire lifecycle of pathology cases — from patient registration at reception through to report dispatch — with full audit trails, billing integration, and digital pathology support.

### Core Workflow Stages

Every case passes through up to 11 workflow stages:

| # | Stage | Description |
|---|-------|-------------|
| 1 | **Received** | Case registered at reception |
| 2 | **Grossing** | Specimen examination and block/slide preparation |
| 3 | **Ready for Processing** | Assigned for tissue processing |
| 4 | **Tissue Processing** | Tissue fixation and dehydration |
| 5 | **Embedding** | Tissue embedded in paraffin wax |
| 6 | **Sectioning** | Thin sections cut from blocks |
| 7 | **Staining** | H&E or special stain application |
| 8 | **Reporting** | Pathologist writes the report |
| 9 | **Consultant Review** | Senior pathologist reviews and signs |
| 10 | **Signed Out** | Report finalized and signed |
| 11 | **Released** | Report dispatched to referring facility |

### Case Types

- **Histopathology** (Prefix: PS) — Tissue biopsy and surgical specimens
- **Cytopathology** (Prefix: PC) — Fine needle aspirates and cytology smears
- **Research** (Prefix: PR) — Research study specimens
- **Postmortem** (Prefix: PM) — Autopsy examinations
- **Other** — Miscellaneous cases

### User Roles

| Role | Access Level |
|------|-------------|
| **Superuser** | Full system access, all admin functions |
| **Administrator** | System configuration, user management, reports |
| **Lab Manager** | Oversight of all lab operations, assignments |
| **Pathologist** | Report writing, review, case assignment |
| **Technician** | Grossing, processing, slide preparation |
| **Accountant** | Billing, invoicing, payments, expenses |
| **Staff** | Basic case viewing, reception duties |
| **Facility** | Facility portal access only |

### Priority Levels

- **STAT** — Immediate processing required (same day)
- **URGENT** — High priority (within 24-48 hours)
- **ROUTINE** — Standard processing (within 7 days)

### TAT (Turnaround Time) Thresholds

- **< 3 days** — Green (on track)
- **3–7 days** — Yellow (approaching limit)
- **> 7 days** — Red (overdue)
- **> 10 days** — Pulsing red (critical)

---

## 2. Getting Started

### Logging In

1. Navigate to the system URL in your web browser
2. You will see the **splash screen** with the PCS LIS logo (first visit only per session)
3. Enter your **username** and **password**
4. Click **Sign In** or press Enter

**Security Features:**
- After 2 failed login attempts, a CAPTCHA verification appears
- After 5 failed attempts, your account is locked for 60 seconds
- If Two-Factor Authentication (2FA) is enabled, you will be prompted for your authenticator code

### The Interface

After login, you see:

- **Sidebar** (left) — Navigation menu with all accessible pages
- **Topbar** (top) — Page title, notification bell, dark mode toggle, refresh button, user profile
- **Main Content** (center) — The current page content
- **Heartbeat Spinner** — Shows briefly when navigating between pages

### Dark Mode

Click the **moon icon** (🌙) in the topbar to toggle between light and dark themes. Your preference is saved per session.

### Command Palette

Press **Ctrl+K** (or **Home** key) to open the global search command palette. Type to search across:
- Case numbers
- Patient names
- Page navigation
- Quick actions

---

## 3. Dashboard

The dashboard is your landing page after login. It shows:

### Stat Cards (Top Row)
- **Total Cases** — All cases in the system
- **Pending** — Cases not yet completed
- **Urgent** — Cases with STAT or URGENT priority
- **Completed Today** — Cases finished today

### Quick Actions
Click any card to jump directly to:
- **New Case Reception** — Register a new specimen
- **Grossing Queue** — Cases awaiting gross examination
- **Processing Queue** — Cases in processing stages
- **Write Reports** — Cases awaiting reports
- **Review Queue** — Cases awaiting consultant review
- **Logbooks** — Histology, cytology, IHC, and research logs

### Workflow Overview
Shows the number of cases at each workflow stage with progress bars.

### Recent Cases
Table of the most recently registered cases with:
- Case number (click to open)
- Patient name
- Hospital/facility
- Current stage
- Priority badge

### Overdue Alerts
Cases that have exceeded the 7-day TAT threshold and have not been dispatched. Each row flashes red to draw attention. The **live TAT countdown** shows real-time elapsed time that updates every 60 seconds.

### Key Metrics
- **Avg TAT** — Average turnaround time for the selected period
- **Completed Today** — Cases finished today
- **In Progress** — Currently active cases
- **Urgent/STAT** — High-priority cases

Use the **TAT range** dropdown to filter: Last 7 days, 30 days, 90 days, this year, or all time.

### Case Volume & TAT Trends
Two charts showing:
- Monthly case volume (bar chart)
- Average TAT over time (line chart)

### My Pending Assignments
Cases specifically assigned to you that are awaiting your action.

---

## 4. Case Reception

The reception page is where new cases are registered.

### Step 1: Select a Facility

1. You see a grid of registered facility cards showing:
   - Facility name and logo
   - Number of cases
   - Outstanding balance
2. **Click a facility card** to register a case for that facility
3. Or click **"Other"** to register for an unregistered facility (type the name manually)

### Step 2: Fill in Case Details

The registration form opens in a modal. Fields marked with * are required.

**Case Information:**
| Field | Description |
|-------|-------------|
| Case Type* | Histopathology, Cytopathology, Research, Postmortem, or Other |
| Path Number | Auto-generated based on case type and year |
| Priority* | ROUTINE, URGENT, or STAT |
| Specimen Type* | Biopsy, Resection, Cytology, Fluid, etc. |
| Clinical History | Free text — relevant clinical information |
| Specimen Received Date* | When the specimen arrived |
| Referring Doctor | Select from registered doctors or add new |

**Patient Information:**
| Field | Description |
|-------|-------------|
| First Name* | Patient's first name |
| Last Name* | Patient's last name |
| Date of Birth* | Used to calculate age automatically |
| Sex* | Male, Female, or Other |
| Phone | Contact number (optional) |
| MRN | Medical Record Number (auto-generated if blank) |

**Referring Doctor:**
- Start typing in the search box to find a registered doctor
- Or click **"Add New Doctor"** to register a new referring doctor with their hospital

### Step 3: Submit

Click **Register Case**. The system will:
1. Generate a unique case number (e.g., PS/0621/26)
2. Create the patient record (or link to existing patient)
3. Create the workflow history entry
4. Redirect you to the case detail page

### Duplicate Detection

The system checks for potential duplicate patients based on name and date of birth. If a match is found, you'll be asked to confirm whether to link to the existing patient or create a new one.

### Path Number Preview

As you type the referring doctor or specimen type, the **Path No.** field updates in real-time showing what the generated case number will be.

---

## 5. Grossing

The grossing stage involves physical examination and processing of specimens.

### Grossing Queue

Navigate to **Grossing** from the sidebar. You see:

- **Filter bar** — Filter by priority, case type, date range
- **Case cards** — Each showing:
  - Case number and patient name
  - Specimen type and priority
  - Date received
  - Pathologist assignment

### Grossing Detail

Click a case card to open the grossing detail page.

**Top Section — Case Info:**
- Case number, patient details, referring doctor
- Priority badge, TAT counter (live), workflow stage

**Specimen Blocks:**
1. Click **"Add Block"** to create a new specimen block
2. Enter block label (e.g., "A1", "B1")
3. Enter tissue description
4. Mark orientation if applicable

**Slides:**
1. For each block, click **"Add Slide"**
2. Enter slide label
3. Select stain type (H&E, Special, IHC, etc.)
4. Mark sections (e.g., "1 of 3")

**Media Upload:**
- Click **"Add Photo"** or **"Add Video"** to upload grossing images
- Supported formats: JPG, PNG, MP4, MOV
- Images are attached to the case for reference

**Findings:**
- Enter gross examination findings in the text area
- Describe specimen dimensions, color, consistency, margins

### Moving to Next Stage

Once grossing is complete:
1. Click **"Move to Processing"** at the bottom
2. Confirm the stage transition
3. The case moves to the Processing queue

---

## 6. Processing

The processing page manages cases through the tissue processing pipeline.

### Tabbed Interface

The processing page has 5 tabs representing the processing sub-stages:

| Tab | Stage | Description |
|-----|-------|-------------|
| **Ready for Processing** | PROCESSING | Newly arrived, awaiting assignment |
| **Tissue Processing** | TISSUE_PROCESSING | Fixation and dehydration in progress |
| **Embedding** | EMBEDDING | Tissue being embedded in paraffin |
| **Sectioning** | SECTIONING | Thin sections being cut |
| **Staining** | STAINING | H&E or special stains being applied |

### Card Layout (Ready for Processing)

The "Ready for Processing" tab shows cases as **cards** with:
- Case number and patient name
- Specimen type
- Priority badge
- Date received
- **Assign** button

### Table Layout (Other Tabs)

The remaining tabs show cases in a **table** with columns:
- Case number
- Patient name
- Specimen type
- Priority
- Pathologist assigned
- Date
- Action buttons

### Assigning a Pathologist

1. Click **"Assign"** on a case card
2. Select a **scientist name** from the dropdown
3. Select a **pathologist** from the dropdown
4. Click **Save Assignment**

### Staining Configuration

On the **Staining** tab, each case has a **"Configure"** button that expands an inline panel with:

- **Scientist Name** — Who is performing the staining
- **Stain Type** — Checkboxes for: H&E, Special Stain, IHC, PAS, mucicarmine, etc.
- **Number of Slides** — How many slides to prepare
- **Assigned Pathologist** — Who will review the stained slides
- Click **"Save & Move"** to complete staining and move to Reporting

### Bulk Stage Transitions

Select multiple cases using checkboxes, then click **"Move Selected"** to advance them all to the next stage simultaneously.

### Auto-Refresh

The queue automatically refreshes every 45 seconds in the background to show newly assigned cases without disrupting your work.

---

## 7. Reporting

The reporting page is where pathologists write diagnostic reports.

### Reporting Queue

Navigate to **Reporting** from the sidebar. You see:

- Cases assigned to you awaiting report writing
- Filter by priority, date range
- Each row shows: case number, patient, specimen type, stage, priority, TAT

### Report Editor

Click **"Write Report"** to open the report editor.

**Top Bar:**
- Case number and patient name
- Priority badge
- TAT counter (live)
- Slide viewer button
- Synoptic panel button
- PDF preview button

**Report Body (Quill Editor):**
A rich text editor with formatting toolbar:
- **Bold**, *Italic*, <u>Underline</u>
- Headings (H1, H2, H3)
- Bullet lists and numbered lists
- Tables
- Undo/Redo

**Report Sections:**
The report is structured into sections:
1. **Clinical History** — Pre-filled from reception
2. **Gross Description** — Pre-filled from grossing
3. **Microscopic Description** — Pathologist writes findings
4. **Diagnosis** — Final diagnostic impression
5. **Comment** — Additional notes or recommendations
6. **IHC Results** — If immunohistochemistry was performed

### Voice Dictation

Click the **microphone icon** to enable voice-to-text dictation. Speak your findings and they will be transcribed into the editor.

**Tips:**
- Speak clearly and at a moderate pace
- Use medical terminology — the system recognizes common pathology terms
- Click the microphone again to stop dictation

### Slide Viewer

Click **"View Slides"** to open the whole-slide image viewer:
- **Zoom** — Scroll wheel or pinch gesture
- **Pan** — Click and drag
- **Annotations** — Draw regions, lines, or points with measurements
- **Contrast** — Adjust brightness/contrast

### Synoptic Panel

Click **"Synoptic"** to open the structured reporting panel:
- Select a template (e.g., Breast Cancer, Colorectal, Prostate)
- Fill in the structured fields
- The assembled text is inserted into the report

### Digital Signatures

Once the report is complete:
1. Click **"Sign Report"**
2. Select your saved signature
3. Enter your password for verification
4. The signature is embedded in the report PDF

### Saving and Submitting

- **Save Draft** — Saves without submitting (you can return later)
- **Submit Report** — Finalizes the report and moves it to Consultant Review
- **PDF Preview** — Generate a preview of the final PDF before submitting

---

## 8. Consultant Review

Senior pathologists review and sign off on reports.

### Review Queue

Navigate to **Review** from the sidebar. Shows:
- Cases awaiting consultant review
- Reporter name
- Case details
- Date submitted

### Review Detail

Click **"Review"** to open the review page:

**Left Side — Report Content:**
- Full report as written by the reporting pathologist
- Synoptic data (if applicable)
- IHC results

**Right Side — Case Info:**
- Patient demographics
- Specimen details
- Workflow history

### Review Actions

**Approve:**
1. Click **"Approve & Sign"**
2. Select your signature
3. Enter password
4. Report moves to "Signed Out"

**Request Amendment:**
1. Click **"Request Amendment"**
2. Type comments explaining what needs to be changed
3. Report returns to the reporting pathologist

**Addendum:**
1. Click **"Add Addendum"**
2. Add supplementary information
3. The addendum is appended to the report with your signature

---

## 9. Dispatch & Sent Reports

### Finalized Reports Center

Navigate to **Finalized** from the sidebar. Shows all signed reports ready for dispatch.

**Tabs:**
- **All** — All finalized reports
- **Histology** — Histopathology reports only
- **Cytology** — Cytopathology reports only
- **IHC** — IHC reports only
- **Postmortem** — Postmortem reports only
- **Research** — Research reports only

### Dispatching Reports

1. Select reports using checkboxes
2. Click **"Dispatch"**
3. Choose dispatch method:
   - **Physical** — Printed and hand-delivered
   - **Email** — Sent via email
   - **Portal** — Available on facility portal
4. Add dispatch remarks
5. Confirm

### Bulk Dispatch

Select multiple reports and click **"Bulk Dispatch"** to dispatch them all at once with the same method and remarks.

### Dispatch Tracking

Navigate to **Dispatched** to see all dispatched reports with:
- Dispatch date and method
- Delivery status (Dispatched, Collected, Delivered, Returned)
- Resend option if delivery failed

### Resending

If a report failed to deliver:
1. Click **"Resend"** on the report
2. Confirm the resend
3. The system will re-send via the original method

---

## 10. Logbooks

Logbooks provide a running record of all cases by type.

### Accessing Logbooks

Navigate to **Logbooks** from the sidebar. You see tabs for:
- **Histology** — All histopathology cases
- **Cytology** — All cytopathology cases
- **IHC** — All immunohistochemistry cases
- **Research** — All research cases
- **Academic** — Academic research cases

### Logbook Table

Each logbook shows a table with:
- Entry number
- Path number (case number)
- Patient name
- Age/Sex
- Date received
- Date completed
- Status (Pending, Completed, Reviewed)
- TAT (turnaround time)

### Inline Editing

Click any editable cell to edit it directly in the table:
- Status changes
- Date updates
- Notes

Press **Enter** to save or **Escape** to cancel.

### Filtering

Use the filter bar above the table to:
- Search by patient name or case number
- Filter by date range
- Filter by status
- Filter by priority

### Cancer Detection

When viewing logbook entries, the system may flag potential cancer cases based on keyword detection rules. A dialog will appear asking you to confirm whether the case should be added to the Cancer Registry.

### Exporting

Click **"Export"** to download the logbook data as:
- Excel spreadsheet (.xlsx)
- CSV file

---

## 11. Cancer Registry

The cancer registry tracks all confirmed cancer cases for reporting and research purposes.

### Registry List

Navigate to **Cancer Registry** from the admin menu. Shows:
- Registry number
- Patient name
- Primary cancer site
- TNM stage
- Registry status (Pending, Confirmed, Incomplete)
- Verification status

### Adding a Case

1. Click **"Add Entry"**
2. Select a case from the dropdown
3. Fill in cancer-specific fields:
   - Primary cancer site
   - Histological type
   - TNM staging (T, N, M)
   - ICD-O code
   - Grade
   - Lymphovascular invasion
   - Perineural invasion
4. Save

### IHC Integration

The registry automatically pulls IHC marker data from the case:
- ER, PR, HER2, Ki-67 scores
- Additional markers (E-Cadherin, AMACR, etc.)

### Verification

Admins can verify registry entries:
1. Open the entry
2. Review all data
3. Click **"Verify"** to confirm accuracy
4. Or click **"Flag"** to mark for correction

### Cancer Detection Rules

Configure automatic cancer detection rules:
- **Keyword rules** — Flag cases containing specific terms (e.g., "malignant", "carcinoma", "adenocarcinoma")
- **Regex rules** — Pattern-based detection
- **ICD-O rules** — Based on diagnosis codes

Rules can be toggled on/off and tested against existing cases.

---

## 12. Immunohistochemistry (IHC)

IHC testing involves staining tissue sections with antibodies to detect specific proteins.

### IHC Log

Navigate to **IHC** tab in Logbooks. Shows:
- IHC number
- Patient name
- Sex/Age
- Antigen tested
- Result
- Status

### IHC Markers

The system supports multi-marker IHC panels:

| Marker | Scoring Method |
|--------|---------------|
| **ER** (Estrogen Receptor) | Allred Score (0-8) |
| **PR** (Progesterone Receptor) | Allred Score (0-8) |
| **HER2** | HER2 Score (0, 1+, 2+, 3+) |
| **Ki-67** | Percentage (0-100%) |
| **E-Cadherin** | Positive/Negative |
| **AMACR** | Positive/Negative |

### Entering IHC Results

1. Open the case detail page
2. Scroll to the IHC section
3. Click **"Add IHC Result"**
4. Select the antigen
5. Enter the score (method depends on marker):
   - **Allred Score**: Enter Proportion (0-5) and Intensity (0-3), system calculates total
   - **HER2 Score**: Select from 0, 1+, 2+, 3+
   - **Ki-67**: Enter percentage
6. Enter interpretation
7. Save

### Auto-IHC Trigger

When a cancer case is flagged in the Cancer Registry, the system can automatically recommend IHC markers based on the cancer type and site.

---

## 13. Synoptic Reporting

Synoptic reporting uses structured templates to ensure consistent, complete pathology reports.

### Templates

Navigate to **Synoptic** from the sidebar. Browse available templates organized by:
- **Organ Site** — Breast, Colon, Prostate, Lung, etc.
- **Category** — Cancer, Benign, Research

### Template Structure

Each template has:
- **Sections** — Logical groupings of fields
- **Fields** — Individual data points to capture
- **Field Types** — Text, dropdown, checkbox, radio, numeric
- **Conditional Fields** — Show/hide based on other field values
- **Required Fields** — Must be completed before submission

### Using a Template

1. Open the report editor for a case
2. Click **"Synoptic"** in the toolbar
3. Select the appropriate template
4. Fill in each field:
   - Dropdowns — Select from predefined options
   - Checkboxes — Check all applicable items
   - Text fields — Type free text
   - Numeric fields — Enter numbers
5. Required fields are highlighted in red if left empty
6. Click **"Insert into Report"**
7. The assembled text is inserted at the cursor position in the report editor

### Saving Drafts

- Click **"Save Draft"** to save your progress without inserting
- Drafts are accessible from the **Drafts** panel
- Load a draft to continue where you left off

### Auto-Fill

For common scenarios, click **"Auto-Fill"** to populate default values:
- Select a preset (e.g., "Typical invasive ductal carcinoma")
- Fields are filled with standard values
- Review and modify as needed

---

## 14. Slide Scanning & Digital Pathology

The system supports whole-slide imaging (WSI) for digital pathology.

### Supported Formats

- **SVS** — Aperio ScanScope
- **TIFF/TIF** — Whole-slide TIFF
- **NDPI** — Hamamatsu
- **MRXS** — 3DHISTECH

### Uploading Scans

1. Navigate to **Slide Manager** or use the staging area
2. Click **"Upload"** or drag files onto the upload zone
3. Files are uploaded in chunks (resumable if interrupted)
4. After upload, the system extracts:
   - Image dimensions (width x height)
   - Number of pyramid levels
   - Magnification
   - File checksum

### Staging Area

New uploads go to the **staging area** (unassigned to any case):
- View all unassigned slides
- See filename, size, dimensions, magnification
- Select slides for assignment

### Assigning Slides to Cases

1. In the staging area, select slides using checkboxes
2. Type the **case number** in the assignment field
3. Click **"Assign Selected"**
4. Slides are moved to the case directory and linked

### Viewing Slides

Click **"View Slide"** on a case to open the **OpenSeadragon viewer**:
- **Zoom** — Scroll wheel, pinch, or +/- buttons
- **Pan** — Click and drag
- **Fit to screen** — Double-click
- **Fullscreen** — Press F11 or click the fullscreen button

### Annotations

In the slide viewer, you can create annotations:
- **Region** — Draw rectangles or freehand regions
- **Line** — Measure distances (in microns)
- **Point** — Mark specific locations
- **Text** — Add labels

Annotations are saved per user and visible to others viewing the same slide.

### Integrity Verification

The system stores a checksum (SHA-256) for each uploaded slide. You can verify file integrity:
1. Open the slide detail
2. Click **"Verify Integrity"**
3. The system compares the current file against the stored checksum
4. Result: **Valid** (file unchanged) or **Corrupted** (file modified)

---

## 15. Billing & Invoicing

The billing system manages invoicing, payments, and financial reporting.

### Billing Dashboard

Navigate to **Billing** from the admin menu. Shows:
- Total revenue
- Outstanding balance
- Paid invoices
- Overdue invoices
- Revenue chart (monthly)

### Case Billing

Each case can be billed individually:

1. Open the case detail page
2. Scroll to the billing section
3. Click **"Update Fee"**
4. Enter:
   - **Base Fee** — Standard service charge
   - **Additional Fees** — Extra charges (e.g., IHC, special stains)
   - **Fee Notes** — Description of charges
5. Click **"Generate Invoice"**

### Fee Schedules

Configure standard pricing by facility type:

| Facility Type | Small Case | Large Case | Cytology | IHC |
|--------------|------------|------------|----------|-----|
| Hospital | GHS X | GHS X | GHS X | GHS X |
| Lab | GHS X | GHS X | GHS X | GHS X |

### Invoicing

Navigate to **Invoices** to see all generated invoices:
- Invoice number
- Case number
- Facility name
- Total amount
- Status (Draft, Pending, Partially Paid, Paid, Overdue)
- Issued date

### Invoice Detail

Click an invoice to see:
- Line item breakdown
- Tax calculation
- Discount applied
- Payment history
- Outstanding balance

### Recording Payments

1. Open the invoice detail
2. Click **"Record Payment"**
3. Enter:
   - Amount
   - Payment method (Cash, Mobile Money, Bank Transfer, Cheque, Insurance)
   - Payment date
   - Reference number
   - Notes
4. Upload proof of payment (optional)
5. Save

The invoice status updates automatically:
- **Paid in full** → Status changes to "Paid"
- **Partial payment** → Status changes to "Partially Paid"
- **Overdue** → Status changes to "Overdue" (past due date)

### Deleting Payments

1. Open the invoice detail
2. Find the payment in the payment history
3. Click the **delete icon** (🗑️)
4. Confirm deletion
5. Invoice totals are recalculated automatically

### Expenses

Track laboratory expenses:
1. Navigate to **Expenses**
2. Click **"Add Expense"**
3. Enter:
   - Category (Supplies, Equipment, Utilities, Salaries, Rent, Transport, Admin)
   - Amount
   - Description
   - Date
4. Save

### Financial Reports

Navigate to **Reports** to view:
- Revenue summary (daily, weekly, monthly, yearly)
- Expense breakdown by category
- Net profit/loss
- Export to Excel or CSV

### Facility Billing View

Navigate to **Facilities** to see:
- Grid of all facilities with outstanding balances
- Click a facility to see:
  - All cases for that facility
  - Invoice and payment history
  - Record payments against specific invoices
  - Status badges (Paid, Outstanding, Overdue)

---

## 16. Facility Portal

The facility portal is a separate login for referring hospitals and labs to view their cases and download reports.

### Facility Login

1. Navigate to the facility portal URL
2. Enter the facility's username and access token
3. Click **Sign In**

### Facility Dashboard

Shows facility-specific stats:
- Total cases submitted
- Cases in progress
- Reports available for download
- Outstanding balance

### Viewing Cases

Navigate to **My Cases** to see all cases submitted by your facility:
- Filter by status, date range, priority
- Click a case to see full details
- View report status

### Downloading Reports

1. Open a case detail
2. Click **"Download Report"**
3. Choose format:
   - **PDF** — Standard report
   - **IHC Report** — Includes IHC results
4. The download is logged for audit purposes

### Bulk Download

Select multiple cases and click **"Bulk Download"** to get a ZIP file containing all selected reports.

### Profile Management

- View facility details
- Change password
- Regenerate access token
- View download history

---

## 17. Administration

The admin portal provides system-level management tools.

### Access

Only users with **Superuser** or **Administrator** roles can access the admin portal.

### Admin Dashboard

Shows system-wide statistics:
- Total users online
- Total cases
- System health indicators
- Recent anomalies

### User Management

Navigate to **Users** to:
- View all system users
- Toggle user active/inactive status
- Change user roles
- Reset passwords
- View activity logs

### Facility Management

Navigate to **Facilities** to:
- View all registered facilities
- Export facility data
- Reset facility passwords
- Regenerate access tokens
- View facility activity logs
- Toggle facility portal access

### Anomaly Detection

The system automatically detects anomalies:
- Cases stuck in a stage for too long
- Unusual billing patterns
- Missing required data
- Duplicate entries

Navigate to **Anomalies** to:
- View detected anomalies
- Mark as resolved
- Bulk resolve multiple anomalies
- Add resolution notes

### Broadcast Messaging

Send announcements to users:
1. Navigate to **Broadcasts**
2. Click **"New Broadcast"**
3. Enter subject and message
4. Choose recipients:
   - All users
   - Specific role
   - Specific users
5. Send

Users see a popup notification when they next load a page.

### Database Backups

Navigate to **Backups** to:
- View existing backups
- Create a new backup (downloads as .sqlite3 file)
- Delete old backups

### Activity Logs

View a complete audit trail of:
- User logins and logouts
- Case modifications
- Report changes
- Billing transactions
- Each entry includes timestamp, user, action, IP address

### Lockdown Mode

In emergencies, enable **Lockdown Mode**:
1. Navigate to **Lockdown**
2. Toggle the switch ON
3. All users except admins see a lockdown screen
4. Music plays during lockdown (configurable)
5. Toggle OFF to restore normal access

---

## 18. AI Assistant — Friday

Friday is an AI-powered assistant integrated into the system.

### Accessing Friday

Click the **Friday icon** in the sidebar or use the chat widget.

### Features

**Chat:**
- Ask questions about cases, patients, or procedures
- Request summaries of patient history
- Get explanations of pathology terms
- Ask for help with report writing

**Quick Actions:**
- "Summarize case PS/0621/26"
- "What are the overdue cases?"
- "Show me today's workload"
- "Help me write a report for [case number]"

**Case Briefings:**
- Request a briefing on a specific case
- Friday compiles: patient history, specimen details, previous reports, IHC results
- Presented in a concise summary format

**Admin Analytics:**
- Ask for productivity reports
- Request workload distribution analysis
- Get TAT performance insights

### Feedback

After each response, you can:
- 👍 — Mark as helpful
- 👎 — Mark as unhelpful
- This feedback helps improve Friday's responses over time

### Privacy

- Friday masks all Protected Health Information (PHI) in responses
- No patient data is stored beyond the current conversation
- Conversations can be cleared at any time

---

## 19. Archiving

Year-end archiving moves completed cases to long-term storage.

### Archive Process

1. Navigate to **Archive** from the admin menu
2. Select the year to archive
3. Review the list of cases to be archived
4. Click **"Start Archive"**
5. The system:
   - Creates a folder structure (Year/Month/CaseNumber)
   - Moves all case files (reports, slides, media)
   - Compresses files into ZIP archives
   - Updates case status to "Archived"

### Accessing Archived Cases

1. Navigate to **Archive**
2. Browse by year → month → case
3. Click a case to view:
   - Report PDF
   - Slide images
   - Media files
   - Case metadata

### Downloading Archived Data

- **Individual case** — Click "Download" on a specific case
- **Bulk download** — Select multiple cases, click "Bulk Download"
- Files are provided as a ZIP archive

### Restoring Archived Cases

If a case needs to be un-archived:
1. Open the archived case
2. Click **"Restore"**
3. The case is moved back to the active database
4. All workflow history is preserved

---

## 20. User Profile & Security

### Profile Page

Navigate to your profile by clicking your name in the topbar.

**Profile Information:**
- Full name
- Email address
- Role
- Phone number
- Avatar/photo

### Changing Your Password

1. Go to **Profile** → **Security**
2. Enter current password
3. Enter new password
4. Confirm new password
5. Click **"Change Password"**

### Digital Signatures

Manage your digital signatures for report signing:

**Adding a Signature:**
1. Go to **Profile** → **Signatures**
2. Click **"Add Signature"**
3. Choose method:
   - **Draw** — Use your mouse/finger to draw on the canvas
   - **Upload** — Upload an image of your signature
   - **Type** — Type your name and select a font style
4. Click **"Save"**

**Setting Default:**
- Click the star icon on a signature to set it as default
- The default signature is pre-selected when signing reports

**Deleting:**
- Click the delete icon on a signature
- Confirm deletion

### Two-Factor Authentication (2FA)

Enhance your account security with TOTP-based 2FA:

**Enabling 2FA:**
1. Go to **Profile** → **Security**
2. Click **"Enable 2FA"**
3. Scan the QR code with your authenticator app (Google Authenticator, Authy, etc.)
4. Enter the 6-digit code from your app
5. Click **"Verify"**
6. Save your **backup codes** in a safe place

**Disabling 2FA:**
1. Go to **Profile** → **Security**
2. Click **"Disable 2FA"**
3. Enter your password
4. Confirm

### Audit Log

View your complete activity history:
- Login/logout times
- Cases accessed
- Reports modified
- Actions performed
- IP addresses

---

## 21. Keyboard Shortcuts & Tips

### Global Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+K** | Open command palette / global search |
| **Home** | Open command palette (alternative) |
| **Esc** | Close any open modal or panel |
| **Ctrl+R** | Refresh current page |

### Report Editor Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+B** | Bold text |
| **Ctrl+I** | Italic text |
| **Ctrl+U** | Underline text |
| **Ctrl+Z** | Undo |
| **Ctrl+Y** | Redo |
| **Ctrl+V** | Paste (from clipboard) |

### Navigation Tips

- **Click the PCS logo** in the sidebar to return to the dashboard
- **Right-click** on case numbers to open in a new tab
- **Hover** over stat cards for detailed tooltips
- **Drag** column headers in tables to resize

### Efficiency Tips

- Use the **command palette** (Ctrl+K) instead of clicking through menus
- **Bulk select** cases in queues for batch operations
- **Pin** frequently used pages in your browser
- Use **voice dictation** for faster report writing
- Set up **2FA** for added security

---

## 22. Troubleshooting

### Common Issues

**"Page not found" (404)**
- Check the URL for typos
- Ensure you have access to that page (your role may not have permission)
- Contact an administrator if the issue persists

**"Permission denied" (403)**
- Your role may not have access to this feature
- Contact your administrator to request access
- Check if your account is active

**"Session expired"**
- Your session timed out due to inactivity
- Log in again
- The system logs you out after 30 minutes of inactivity

**"Case number already exists"**
- The case was already registered
- Search for the existing case using the command palette
- Check with reception if unsure

**Report PDF not generating**
- Ensure all required fields are completed
- Check that the report has been signed
- Try refreshing the page and trying again

**Slide viewer not loading**
- Ensure the slide file was uploaded successfully
- Check your internet connection (slides can be large files)
- Try a different browser

**WhatsApp messages not sending**
- Check the WhatsApp configuration in admin settings
- Verify the recipient's phone number format
- Check the delivery status in the dispatch log

**Billing totals incorrect**
- Verify all payments are correctly recorded
- Check for deleted payments that may have affected totals
- Use the "Refresh Totals" function in the billing settings

### Performance Tips

- Close unused browser tabs to free memory
- Clear your browser cache periodically
- Use Chrome or Edge for best performance
- Ensure a stable internet connection for slide viewing

### Getting Help

- **In-app help** — Click the question mark icon (?) in the topbar
- **Friday AI** — Ask the AI assistant for help with any feature
- **Admin support** — Contact your system administrator
- **System logs** — Check the admin portal → Activity Logs for errors

---

## Appendix A: Case Number Format

Case numbers follow the format: **PREFIX/SEQUENTIAL/YEAR**

Examples:
- `PS/0621/26` — Histopathology case #621, year 2026
- `PC/0145/26` — Cytopathology case #145, year 2026
- `PR/0012/26` — Research case #12, year 2026
- `PM/0003/26` — Postmortem case #3, year 2026

The sequential number auto-increments per prefix per year.

## Appendix B: Status Codes

### Workflow Stages
`RECEIVED`, `GROSSING`, `PROCESSING`, `TISSUE_PROCESSING`, `EMBEDDING`, `SECTIONING`, `STAINING`, `REPORTING`, `CONSULTANT_REVIEW`, `SIGNED_OUT`, `RELEASED`

### Dispatch Statuses
`READY`, `DISPATCHED`, `COLLECTED`, `DELIVERED`, `RETURNED`, `CANCELLED`

### Invoice Statuses
`DRAFT`, `PENDING`, `PARTIALLY_PAID`, `PAID`, `OVERDUE`, `CANCELLED`

### Logbook Statuses
`pending`, `completed`, `reviewed`

### Cancer Registry Status
`Pending`, `Confirmed`, `Incomplete`

### Verification Status
`Unverified`, `Verified`, `Flagged`

## Appendix C: Glossary

| Term | Definition |
|------|-----------|
| **TAT** | Turnaround Time — days from specimen receipt to report dispatch |
| **H&E** | Hematoxylin and Eosin — standard tissue stain |
| **IHC** | Immunohistochemistry — antibody-based protein detection |
| **TNM** | Tumor, Node, Metastasis — cancer staging system |
| **Allred Score** | Scoring system for ER/PR expression (0-8) |
| **HER2** | Human Epidermal Growth Factor Receptor 2 |
| **Ki-67** | Cell proliferation marker |
| **MRN** | Medical Record Number |
| **WSI** | Whole-Slide Image |
| **DZI** | Deep Zoom Image — tiled format for large images |
| **Synoptic** | Structured reporting format with predefined fields |
| **Grossing** | Macroscopic examination of specimens |
| **Embedding** | Infiltrating tissue with paraffin for sectioning |
| **Sectioning** | Cutting thin slices from embedded tissue blocks |
| **Dispatch** | Sending completed reports to referring facilities |

---

*PCS LIS User Guide — Version 2.0*
*Pathology Consultancy Services*
*Last Updated: September 2026*
