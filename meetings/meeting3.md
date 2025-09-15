# Meeting 3

04 ‎September ‎2025, ‏‎12:01:00  

## Overview  

**Attendance:** Max, Ozzy, Michał.  

#### Acknowledgements:  

- Max confirmed the project is ahead of schedule.  
- Progress on the pipeline (IOC loader → hash utils → scanner) is nearly complete.  

#### Progress Updates:  

- **Max:**  
  - Completed **scanner** (with placeholders for hash utils).  
  - Will also handle the **metadata collector** (expected within 2 weeks).  
- **Ozzy:**  
  - Finished **IOC loader**.  
  - Next: **extension filter**, due by **11 October**.  
- **Michał:**  
  - Working on **hash utils** (expected to complete the same day).  
  - Will later move on to **report.py**, dependent on completion of the extension filter and metadata collector.  

#### Upcoming Work & Deadlines:  

- **Ozzy:** Complete **extension filter** by 11 October.  
- **Max:** Complete **metadata collector** within 2 weeks.  
- **Michał:** Finish **hash utils** immediately, then begin **report.py** once dependencies are ready.  

#### Blockers / Concerns:  

- No blockers reported.  
- No access or tool issues raised.  

#### Recap:  

- Ozzy → extension filter (by 11 October).  
- Michał → hash utils, then report.py.  
- Max → metadata collector, scanner integration.  

Closing: Team confirmed alignment, no issues.  

---

## Transcript  

**Max Z. 0:00**  
Right, let’s get started. This won’t take long. So, to begin — the project is ahead of schedule, which is excellent. The core data stream is nearly complete: IOC loader to hash utils to scanner, so soon everything will flow end-to-end.  

What’s left: Michał, if hash utils isn’t finished yet, please wrap that up. We also have the extension filter, metadata collector, and then the report later on.  

Ozzy, you’ve already finished the IOC loader, so your next task is the extension filter. Since we’re ahead of schedule, you can take it at a steady pace.  

**Ozzy A. 1:00**  
When’s it due?  

**Max Z. 1:03**  
The extension filter is due 11 October.  

**Ozzy A. 1:07**  
Alright, so there’s time.  

**Max Z. 1:10**  
I finished the scanner last night, with placeholders for hash utils. So, I’m ready to integrate hash utils into it once that’s ready. Michał, where are you with hash utils?  

**Michał T. 1:21**  
It should be done today. I was working out how to process it in chunks. I thought the update just added to the data, but it seems it can handle chunking, and it works fine.  

**Max Z. 1:39**  
Okay, that’s good. I’ll test it — any problems will come up during testing, but that’s further down the line.  

**Ozzy A. 1:53**  
Perfect. If it’s not done today, that’s fine.  

**Max Z. 1:57**  
Brilliant. Again, we’re ahead of schedule. The focus is on finishing features, not testing. Testing will be done all together once everything is complete — it’ll be simple, so no need for partial testing.  

So, current milestones: extension filter (Ozzy), metadata collector (me), hash utils integration into scanner once Michał’s done. After all that, we’ll test the pipeline as a whole.  

Any problems or access issues?  

**[Silence]**  

**Max Z. 2:59**  
Alright, just to recap:  
- Ozzy, extension filter due 11 October.  
- I’ll complete metadata collector within 2 weeks.  
- Michał, hash utils today, then report.py afterwards. You’ll need to wait until the extension filter and metadata collector are done, but you can use placeholders in the meantime.  

**Michał T. 3:33**  
Yes, I’ll need to see how everything works anyway for the report.  

**Max Z. 3:37**  
Exactly. Report.py isn’t too bad; the tricky bit is handling multiple outputs (CSV, Python). But you’ll manage.  

That’s all from me. Anything else?  

**[Silence]**  

**Max Z. 3:59**  
Perfect. Thanks, everyone. Have a nice day!  
