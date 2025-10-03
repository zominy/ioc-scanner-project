# Meeting 4

20 ‎August ‎2025, ‏‎11:00:00

### Note

Meeting 1 was corrupted in recording. For those looking for Sofiane’s introduction, it is very similar — Max uses the same presentation each time a new member joins.

### Overview

Attendance: Max, Sofiane (new member), later joined by Ozzy and Michał.

### Acknowledgements:

Max officially welcomed Sofiane Laleg.

Project is ahead of schedule; only report.py remains as a core deliverable.

Progress Updates:

### Max:

- Delivered the project introduction and walkthrough to Sofiane.

- Confirmed scanner, metadata collector, and extension filter are complete.

- Clarified that main.py will be built after report.py is finished.

### Ozzy:

- Completed extension filter.

### Michał:

- Completed hash utils.

- Will support Sofiane on report.py.

### Sofiane:

- Assigned to report.py.

- Onboarded to the GitHub workflow and coding standards.

### Upcoming Work & Deadlines:

Sofiane & Michał: Complete report.py (expected within 2 weeks).

Max: Begin main.py after report.py completion.

Ozzy: Support as required.

### Blockers / Concerns:

None raised.

Sofiane to finish GitHub setup after the meeting.

### Recap:

Sofiane & Michał (Support) → report.py.

Max → main.py (after report.py).

Ozzy → support.

Next meeting in 2 weeks.

# Transcript

Max Z. 0:00
Right, let’s get started. I’ll give you an overview of the project. We had an initial presentation that explains the overall structure and logic, so I’ll run you through it.

Max Z. 0:29
By the end of this project you’ll be working with real-world cybersecurity tools and logic used by professionals. You’ll learn how to detect malware using Indicators of Compromise (IOCs), and how to write Python code that is clean and well documented.

We work collaboratively like a development team. There are three of us already, and we each handle different parts of the system. If you remember from modular programming, each of us manages separate files which integrate together.

We also do code reviews — that’s coming soon — plus integration and version control. By the end you’ll have a project you can showcase for Year 3 placement, or even use to land a job.

Max Z. 1:42
An IOC is an indicator of compromise, a digital fingerprint of something malicious. In this project we hash files and check them against known bad hashes. If there’s a match, the system flags it and collects metadata.

Hashing is running data through an algorithm to produce a fixed-length string unique to that file. Change even one byte, and the hash changes completely. It’s widely used in security for file integrity and malware detection.

Sofiane L. 5:02
What’s the reason for hashing some text or data?

Max Z. 5:09
Say you send an important document to your boss. Hashing proves that it hasn’t been changed en route. It verifies integrity.

Here, the scanner takes a file path, scans the file, creates a hash, and compares it with known IOCs. If it matches, we flag it, collect metadata, and add it to a report.

The IOC list comes from threat intelligence feeds or repositories. The scanner can handle single files or full directories, recursively checking subfolders. It uses SHA-256 to fingerprint each file.

If the hash matches, we log it with metadata such as file size, creation and modification dates, permissions, and path. The results are compiled into a report.

Max Z. 10:00
Assignments so far:

Ozzy has completed the IOC loader and extension filter.

Michał finished hash utils.

I’ve completed the scanner and metadata collector.

The only major file left is report.py, which Sofiane, you’ll work on with Michał.

Max Z. 12:00
We’ll be using GitHub for collaboration. After each module is finished, you’ll push it. Code must be clear and documented — with docstrings, inline comments, and readable variable names. Reviews ensure code can be understood by anyone new who joins.

[Ozzy and Michał join the meeting]

Michał T. 15:50
Hi everyone, can you hear me?

Max Z. 15:55
Yes. So, update: Ozzy has completed the extension filter. The only piece left is report.py, which Michał and Sofiane will complete together.

Once that’s done, we’ll move to code reviews. Report.py isn’t too large — maybe 20–25 lines — but you’ll need to support both TXT and CSV outputs and integrate metadata.

While that’s in progress, I’ll prepare for main.py, but that will only be done after report.py is completed.

Ozzy A. 16:10
Understood.

Max Z. 16:12
Do you think two weeks is enough for report.py?

Sofiane L. 16:15
Yes, that’s fine.

Max Z. 16:18
Good. Sofiane, I’ll send you the GitHub setup guide and add you to the repository. Once you accept, you’ll be able to start.

Sofiane L. 16:23
Yes, I’ll send you my username.

Max Z. 16:24
Perfect. That’s everything for today. Next meeting in two weeks to review progress. (Meeting 5 postponed due to time extensions)
