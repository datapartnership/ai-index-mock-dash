# Align the mock's IWAs with what Option 4a sampling can deliver (see mock_iwa_reach.md).
import sys,io
P='js/dashboard-engine.js'; s=open(P,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt, (n,a[:90]); s=s.replace(a,b)
# --- names used across the main page (real O*NET IWA titles, all reportable each quarter on all conversations)
REN={'Write material for commercial or creative purposes':'Write material for artistic or commercial purposes',
 'Program computer systems or applications':'Program computer systems or production equipment',
 'Translate or interpret information':'Interpret language, cultural, or religious information for others',
 'Prepare instructional or informational materials':'Prepare informational or instructional materials',
 'Explain technical or academic concepts':'Explain technical details of products or services'}
for a,b in REN.items(): s=s.replace("'"+a+"'","'"+b+"'")
R("'Analyze data to inform decisions','Edit written materials or documents','Explain technical details of products or services','Research laws, regulations or precedents','Develop marketing or sales content','Advise others on personal or health matters']",
  "'Analyze data to improve operations','Edit written materials or documents','Explain technical details of products or services','Explain regulations, policies, or procedures','Develop marketing or promotional materials','Advise others on healthcare or wellness issues']")
# GWAs: replace 'Updating and using relevant knowledge' (no IWA reportable by country) with the largest GWA, which the mock omitted
R("'Interpreting the meaning of information for others','Updating and using relevant knowledge'];\nconst GWA_W = [16, 14, 12, 11, 10, 9, 9, 8, 6, 5];",
  "'Interpreting the meaning of information for others','Providing consultation and advice to others'];\nconst GWA_W = [13, 9, 12, 6, 12, 2, 3, 7, 3, 24];   // roughly Claude.ai shares (Anthropic Economic Index)")
i0=s.index('const WA_TREE = {'); i1=s.index('};',i0)+2
s=s[:i0]+'''const WA_TREE = {   // O*NET IWAs under each GWA that the sampling standard can report by country each quarter; weights roughly Claude.ai shares
  'Getting information': [['Gather information from physical or electronic sources', 11.9], ['Read documents or materials to inform work processes', 0.3]],
  'Working with computers': [['Resolve computer problems', 3.4], ['Program computer systems or production equipment', 3.1], ['Process digital or online data', 2.6]],
  'Thinking creatively': [['Design computer or information systems or applications', 2.6], ['Develop marketing or promotional materials', 2.2], ['Create visual designs or displays', 2.0], ['Develop news, entertainment, or artistic content', 1.8], ['Develop business or marketing plans', 0.8]],
  'Analyzing data or information': [['Analyze data to improve operations', 2.1], ['Analyze scientific or applied data using mathematical principles', 1.2], ['Analyze market or industry conditions', 0.8], ['Evaluate designs, specifications, or other technical data', 0.6]],
  'Documenting and recording information': [['Prepare informational or instructional materials', 4.1], ['Write material for artistic or commercial purposes', 3.5], ['Present research or technical information', 1.5], ['Maintain operational records', 0.8]],
  'Communicating with people outside the organization': [['Respond to customer problems or inquiries', 2.0]],
  'Training and teaching others': [['Teach academic or vocational subjects', 2.9]],
  'Making decisions and solving problems': [['Edit written materials or documents', 5.3], ['Diagnose system or equipment problems', 1.0]],
  'Interpreting the meaning of information for others': [['Explain technical details of products or services', 1.3], ['Interpret language, cultural, or religious information for others', 1.0], ['Explain regulations, policies, or procedures', 0.6], ['Explain medical information to patients or family members', 0.3]],
  'Providing consultation and advice to others': [['Advise others on the design or use of technologies', 6.2], ['Advise others on products or services', 6.0], ['Counsel others about personal matters', 2.4], ['Advise patients or clients on medical issues', 2.4], ['Advise others on business or operational matters', 2.1], ['Advise others on financial matters', 1.7]]
};'''+s[i1:]
R("${d.iwas.length} intermediate work activities (IWAs) sit under this work activity. Together they make up ${d.share}% of work-related conversations.",
  "${d.iwas.length === 1 ? 'One intermediate work activity (IWA)' : d.iwas.length + ' intermediate work activities (IWAs)'} under this work activity can be reported for each country every quarter; rarer ones are published half-yearly, annually or by region. Together the work activity makes up ${d.share}% of conversations.")
# sample captions: Option 4a quotas, four firms combined
R("sample: 'Sample: about 240,000 conversations this quarter. All cross-tabs are available.'",
  "sample: 'Sample: about 400,000 classified conversations this quarter (100,000 per firm, four firms; tier 1). All cross-tabs are available.'")
R("sample: 'Sample: about 6,100 conversations this quarter. Two of three cross-tabs are suppressed for statistical disclosure control, and API estimates carry wide uncertainty.'",
  "sample: 'Sample: Malawi is pooled each quarter with six Eastern African neighbours (about 80,000 classified conversations for the group: 20,000 per firm, four firms). Country figures shown are annual where firms’ volumes allow. Two of three cross-tabs are suppressed for statistical disclosure control, and API estimates carry wide uncertainty.'")
R("sample: 'Sample: about 1.9 million conversations this quarter. All cross-tabs are available.",
  "sample: 'Sample: about 400,000 classified conversations this quarter (100,000 per firm, four firms; tier 1). All cross-tabs are available.")
# public-service cross-tab (Jobs and skills view): real IWA titles
R("const PUB_IWA = ['Draft official correspondence','Summarize laws and regulations','Translate public information','Analyze program data','Respond to citizen enquiries','Prepare budgets and reports'];",
  "const PUB_IWA = ['Explain regulations, policies, or procedures','Prepare documentation for contracts, applications, or permits','Interpret language, cultural, or religious information for others','Analyze data to improve operations','Respond to customer problems or inquiries','Prepare informational or instructional materials'];   // IWA x industry cells: annual, four quarters pooled")
R("'IWA by industry: public service activities (% of public-sector conversations)'","'IWA by industry: public service activities (% of public-sector conversations, four quarters pooled)'")
# questions page: sampling note
R("const QX_MIN = 'Sample size. The live Index hides cells below a minimum amount of activity, and how many detailed activities it can report depends on each country’s sample, so fine cuts may need quarters or categories pooled.';",
  "const QX_MIN = 'Sample size. Under the sampling standard (100 conversations per cell), countries outside the 12 high-usage countries can report about 42 activities each quarter, 53 with two quarters pooled and 69 with a year. Activities within an occupation, industry or use type are smaller cells: they are published annually by country or quarterly by region, and the rarest only by region.';")
# Q2 teaching activities: drop two that cannot be reported; annual by country
R("const acts = [['Develop educational programs, plans, or procedures', [7, 12, 8]], ['Teach academic or vocational subjects', [8, 10, 4]], ['Assess student capabilities, needs, or performance', [5, 8, 4]], ['Collaborate in the development of educational programs', [3, 4, 2]], ['Advise others on educational or vocational matters', [2, 3, 1]], ['Teach life skills', [2, 2, 1]]];\n      const short = ['Planning lessons and programs', 'Teaching subject content', 'Assessing students', 'Developing programs with colleagues', 'Advising students', 'Teaching life skills'];",
  "const acts = [['Prepare informational or instructional materials', [7, 12, 8]], ['Teach academic or vocational subjects', [8, 10, 4]], ['Advise others on educational or vocational matters', [5, 8, 4]], ['Assess student capabilities, needs, or performance', [3, 4, 2]], ['Develop educational programs, plans, or procedures', [2, 3, 1]]];\n      const short = ['Preparing teaching materials', 'Teaching subject content', 'Advising students', 'Assessing students', 'Planning lessons and programs'];")
R("sub: 'Share of the teaching topic’s work-related AI activity (%), by O*NET IWA. Other activities, such as email, make up the rest.'",
  "sub: 'Share of the teaching topic’s work-related AI activity (%), by O*NET IWA, latest four quarters pooled. Other activities make up the rest.'")
R("alt: `Bar chart for ${CX}: six teaching-related work activities by share of the teaching topic’s AI activity.`","alt: `Bar chart for ${CX}: five teaching-related work activities by share of the teaching topic’s AI activity, four quarters pooled.`")
R("{ k: 'c', t: 'Teaching-related IWAs', d: 'e.g. Develop educational programs, plans, or procedures; Teach academic or vocational subjects; Assess student capabilities, needs, or performance' }",
  "{ k: 'c', t: 'Teaching-related IWAs', d: 'e.g. Prepare informational or instructional materials; Teach academic or vocational subjects; Assess student capabilities, needs, or performance. Annual by country, quarterly by region' }")
# Q3 part b: the five largest IWAs in each occupation that can be reported annually by country
NEWB={'Information and communications technology':['Advise others on the design or use of technologies','Resolve computer problems','Design computer or information systems or applications','Program computer systems or production equipment','Process digital or online data'],
'Business and administration':['Advise others on financial matters','Develop marketing or promotional materials','Analyze data to improve operations','Advise others on business or operational matters','Analyze market or industry conditions'],
'Science and engineering':['Analyze scientific or applied data using mathematical principles','Design computer or information systems or applications','Present research or technical information','Create visual designs or displays','Program computer systems or production equipment'],
'Management':['Advise others on products or services','Develop marketing or promotional materials','Analyze data to improve operations','Advise others on business or operational matters','Respond to customer problems or inquiries'],
'Clerical support':['Gather information from physical or electronic sources','Respond to customer problems or inquiries','Process digital or online data','Provide information to guests, clients, or customers','Explain technical details of products or services'],
'Teaching':['Prepare informational or instructional materials','Teach academic or vocational subjects','Advise others on educational or vocational matters','Assess student capabilities, needs, or performance','Develop educational programs, plans, or procedures'],
'Service and sales':['Advise others on products or services','Respond to customer problems or inquiries','Provide information to guests, clients, or customers','Prepare informational or instructional materials','Explain technical details of products or services'],
'Health':['Advise patients or clients on medical issues','Advise others on healthcare or wellness issues','Analyze health or medical data','Explain medical information to patients or family members','Prepare informational or instructional materials']}
import re
for topic,names in NEWB.items():
    k=s.index("{ id: '"+topic+"', rows: [")
    e=s.index("] }",k)
    seg=s[k:e]
    vals=re.findall(r"\['[^']*', (\d+), (\d+), (\d+)\]",seg)
    assert len(vals)==5,(topic,vals)
    rows=', '.join(f"['{n}', {a}, {b}, {c}]" for n,(a,b,c) in zip(names,vals))
    s=s[:k]+"{ id: '"+topic+"', rows: ["+rows+s[e:]
R("sub: 'Share of the occupation’s work-related AI activity (%), five largest O*NET intermediate work activities (IWAs)'",
  "sub: 'Share of the occupation’s work-related AI activity (%), five largest O*NET intermediate work activities (IWAs), latest four quarters pooled'")
# Q7 business-running activities: replace those too rare to report; annual by country
i0=s.index("const A = [['Develop marketing or promotional materials', 2.1, 3.0]"); i1=s.index("];",i0)+2
s=s[:i0]+"const A = [['Develop marketing or promotional materials', 2.1, 3.0], ['Respond to customer problems or inquiries', 1.8, 2.4], ['Advise others on business or operational matters', 1.2, 1.7], ['Analyze market or industry conditions', 1.0, 1.3], ['Develop business or marketing plans', 0.9, 1.4], ['Calculate financial data', 0.6, 0.8], ['Develop financial or business plans', 0.5, 0.6], ['Analyze business or financial data', 0.4, 0.6]];"+s[i1:]
R("series: [{ name: '2025 Q1', color: RAMP[1], data: A.map(x => x[1]) }, { name: '2026 Q3', color: 'consumer', data: A.map(x => x[2]) }],\n          title: `Business-running activities in work-related AI use in ${CX}`, sub: 'Share of work-related consumer AI activity (%), by O*NET intermediate work activity'",
  "series: [{ name: 'Year to 2025 Q4', color: RAMP[1], data: A.map(x => x[1]) }, { name: 'Year to 2026 Q3', color: 'consumer', data: A.map(x => x[2]) }],\n          title: `Business-running activities in work-related AI use in ${CX}`, sub: 'Share of work-related consumer AI activity (%), by O*NET intermediate work activity; four quarters pooled'")
R("alt: `Horizontal bar chart for ${CX}: eight business-running work activities, share of work-related AI activity in 2025 Q1 and 2026 Q3.`","alt: `Horizontal bar chart for ${CX}: eight business-running work activities, share of work-related AI activity in the years to 2025 Q4 and 2026 Q3.`")
R("{ k: 'c', t: 'Business-running work activities (O*NET IWAs)', d: 'e.g. Develop marketing or promotional materials; Respond to customer problems or inquiries; Maintain sales or financial records' }",
  "{ k: 'c', t: 'Business-running work activities (O*NET IWAs)', d: 'e.g. Develop marketing or promotional materials; Respond to customer problems or inquiries; Calculate financial data. Annual by country' }")
R("`Together these eight activities went from ${t0}% to ${t1}% of work-related AI activity in ${CX}. Marketing materials and customer inquiries are the largest; “${A[gi][0]}” grew fastest (+${g[gi]}%).`",
  "`Together these eight activities went from ${t0}% to ${t1}% of work-related AI activity in ${CX}, comparing the years to 2025 Q4 and 2026 Q3. Marketing materials and customer inquiries are the largest; “${A[gi][0]}” grew fastest (+${g[gi]}%).`")
# Q8 part c: personal paperwork is only reportable by region
R("{ k: 'c', t: 'Personal use by work activity', d: 'paperwork and public-records activities (proxy, part c)' }",
  "{ k: 'c', t: 'Personal use by work activity', d: 'paperwork and rules activities (proxy, part c); by region, too rare to report by country' }")
R("subC: 'Citizens dealing with government: a proxy',","subC: 'Citizens dealing with government: a proxy, for the region',")
R("series: [{ name: 'Prepare documentation for contracts, applications, or permits', color: 'consumer', data: pp }, { name: 'Consult legal materials or public records', color: RAMP[2], data: pr, dash: true }],\n          title: `Paperwork and public records in personal AI use, ${CX}`, sub: 'Share of personal consumer AI activity (%), by quarter', src: 'Index: personal use type, O*NET intermediate work activities (proxy). Values are illustrative.', alt: `Line chart for ${CX}: two paperwork-related activities as a share of personal AI activity, by quarter.` },",
  "series: [{ name: 'Prepare documentation for contracts, applications, or permits', color: 'consumer', data: pp }, { name: 'Explain regulations, policies, or procedures', color: RAMP[2], data: pr, dash: true }],\n          title: `Paperwork and rules in personal AI use, ${CX}’s region`, sub: 'Share of personal consumer AI activity (%), by quarter, all countries in the region pooled', src: 'Index: personal use type, O*NET intermediate work activities (proxy), regional aggregate; too rare to report by country. Values are illustrative.', alt: `Line chart for ${CX}’s region: two paperwork-related activities as a share of personal AI activity, by quarter.` },")
R("`Preparing documentation for contracts, applications or permits went from ${pp[0]}% to ${pp[L]}% of personal AI activity in ${CX}.`",
  "`Across ${CX}’s region, preparing documentation for contracts, applications or permits went from ${pp[0]}% to ${pp[L]}% of personal AI activity. Too few such conversations are sampled to report it for ${CX} alone.`")
open(P,'w',encoding='utf-8').write(s)
# index.html wording: the work-activity views use all conversations so that they can be reported each quarter
H='index.html'; h=open(H,encoding='utf-8').read()
def RH(a,b):
    global h
    assert h.count(a)==1,a[:80]; h=h.replace(a,b)
RH("Share of work-related conversations by O*NET work activity. Each general work activity (GWA) contains several intermediate work activities (IWAs).",
   "Share of all sampled conversations (work, personal and education) by O*NET work activity, this quarter. Each general work activity (GWA) contains intermediate work activities (IWAs); those shown can be reported for every country each quarter.")
RH("The ten largest intermediate work activities (IWAs) across all work activities, share of work-related conversations (%).",
   "The ten largest intermediate work activities (IWAs) across all work activities, share of all sampled conversations (%). Shares of work-related conversations only are published half-yearly.")
RH("Top 10 intermediate work activities by share of work-related conversations.","Top 10 intermediate work activities by share of all sampled conversations.")
RH("Choose an occupational topic to see which intermediate work activities (IWAs) its conversations are about.",
   "Choose an occupational topic to see which intermediate work activities (IWAs) its conversations are about. Activities within an occupation are smaller cells, so they are published annually by country (four quarters pooled) and quarterly by region.")
open(H,'w',encoding='utf-8').write(h)
print('ok')
