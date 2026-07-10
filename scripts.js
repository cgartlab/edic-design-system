/* ===== EDIC Design System v1.9.1 — Icon Grid & Token Table ===== */

const ICONS = [
  {id:"archive",svg:'<svg viewBox="0 0 24 24"><polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/></svg>'},
  {id:"arrow-down",svg:'<svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/></svg>'},
  {id:"arrow-left",svg:'<svg viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>'},
  {id:"arrow-right",svg:'<svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'},
  {id:"arrow-up",svg:'<svg viewBox="0 0 24 24"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 19 5 12"/></svg>'},
  {id:"at-sign",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M16 12v1.5a2.5 2.5 0 0 0 5 0V12a9 9 0 1 0-5.5 8.3"/></svg>'},
  {id:"bar-chart",svg:'<svg viewBox="0 0 24 24"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>'},
  {id:"bell",svg:'<svg viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>'},
  {id:"bookmark",svg:'<svg viewBox="0 0 24 24"><polyline points="19 21 12 17 5 21 5 3 19 3 19 21"/></svg>'},
  {id:"box",svg:'<svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'},
  {id:"briefcase",svg:'<svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>'},
  {id:"calendar",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'},
  {id:"camera",svg:'<svg viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>'},
  {id:"check",svg:'<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'},
  {id:"check-circle",svg:'<svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'},
  {id:"chevron-down",svg:'<svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>'},
  {id:"chevron-left",svg:'<svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>'},
  {id:"chevron-right",svg:'<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>'},
  {id:"chevron-up",svg:'<svg viewBox="0 0 24 24"><polyline points="18 15 12 9 6 15"/></svg>'},
  {id:"circle",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>'},
  {id:"clipboard",svg:'<svg viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'},
  {id:"clock",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'},
  {id:"cloud",svg:'<svg viewBox="0 0 24 24"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9z"/></svg>'},
  {id:"code",svg:'<svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'},
  {id:"copy",svg:'<svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'},
  {id:"credit-card",svg:'<svg viewBox="0 0 24 24"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>'},
  {id:"delete",svg:'<svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>'},
  {id:"download",svg:'<svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'},
  {id:"edit",svg:'<svg viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>'},
  {id:"external-link",svg:'<svg viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'},
  {id:"eye",svg:'<svg viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'},
  {id:"file",svg:'<svg viewBox="0 0 24 24"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><polyline points="13 2 13 9 20 9"/></svg>'},
  {id:"file-text",svg:'<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'},
  {id:"filter",svg:'<svg viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>'},
  {id:"flag",svg:'<svg viewBox="0 0 24 24"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>'},
  {id:"folder",svg:'<svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>'},
  {id:"gift",svg:'<svg viewBox="0 0 24 24"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>'},
  {id:"globe",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'},
  {id:"grid",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>'},
  {id:"hash",svg:'<svg viewBox="0 0 24 24"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>'},
  {id:"heart",svg:'<svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'},
  {id:"help-circle",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'},
  {id:"home",svg:'<svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'},
  {id:"image",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'},
  {id:"info",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'},
  {id:"key",svg:'<svg viewBox="0 0 24 24"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.78 7.78 5.5 5.5 0 0 1 7.78-7.78zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/></svg>'},
  {id:"layers",svg:'<svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'},
  {id:"layout",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>'},
  {id:"link",svg:'<svg viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>'},
  {id:"list",svg:'<svg viewBox="0 0 24 24"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>'},
  {id:"lock",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'},
  {id:"mail",svg:'<svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>'},
  {id:"map-pin",svg:'<svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'},
  {id:"maximize",svg:'<svg viewBox="0 0 24 24"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>'},
  {id:"menu",svg:'<svg viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>'},
  {id:"mic",svg:'<svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>'},
  {id:"minimize",svg:'<svg viewBox="0 0 24 24"><path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/></svg>'},
  {id:"minus",svg:'<svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/></svg>'},
  {id:"monitor",svg:'<svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>'},
  {id:"moon",svg:'<svg viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'},
  {id:"more-horizontal",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>'},
  {id:"more-vertical",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="12" cy="19" r="1"/></svg>'},
  {id:"move",svg:'<svg viewBox="0 0 24 24"><polyline points="5 9 2 12 5 15"/><polyline points="9 5 12 2 15 5"/><polyline points="15 19 12 22 9 19"/><polyline points="19 9 22 12 19 15"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="12" y1="2" x2="12" y2="22"/></svg>'},
  {id:"music",svg:'<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>'},
  {id:"package",svg:'<svg viewBox="0 0 24 24"><path d="M16.5 9.4L7.55 4.24"/><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'},
  {id:"paperclip",svg:'<svg viewBox="0 0 24 24"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>'},
  {id:"pause",svg:'<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>'},
  {id:"phone",svg:'<svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'},
  {id:"play",svg:'<svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>'},
  {id:"plus",svg:'<svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'},
  {id:"power",svg:'<svg viewBox="0 0 24 24"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"/><line x1="12" y1="2" x2="12" y2="12"/></svg>'},
  {id:"search",svg:'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'},
  {id:"send",svg:'<svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>'},
  {id:"server",svg:'<svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>'},
  {id:"settings",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>'},
  {id:"share",svg:'<svg viewBox="0 0 24 24"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>'},
  {id:"shield",svg:'<svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'},
  {id:"shopping-cart",svg:'<svg viewBox="0 0 24 24"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>'},
  {id:"sidebar",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>'},
  {id:"sliders",svg:'<svg viewBox="0 0 24 24"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>'},
  {id:"smile",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>'},
  {id:"speaker",svg:'<svg viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="14" r="4"/><line x1="12" y1="6" x2="12.01" y2="6"/></svg>'},
  {id:"star",svg:'<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'},
  {id:"sun",svg:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'},
  {id:"table",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>'},
  {id:"tag",svg:'<svg viewBox="0 0 24 24"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>'},
  {id:"terminal",svg:'<svg viewBox="0 0 24 24"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>'},
  {id:"trash",svg:'<svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>'},
  {id:"trending-up",svg:'<svg viewBox="0 0 24 24"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>'},
  {id:"unlock",svg:'<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>'},
  {id:"upload",svg:'<svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>'},
  {id:"user",svg:'<svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'},
  {id:"users",svg:'<svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'},
  {id:"video",svg:'<svg viewBox="0 0 24 24"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>'},
  {id:"volume",svg:'<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>'},
  {id:"wifi",svg:'<svg viewBox="0 0 24 24"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>'},
  {id:"x",svg:'<svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'},
  {id:"zap",svg:'<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'},
  {id:"zoom-in",svg:'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>'},
  {id:"zoom-out",svg:'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="8" y1="11" x2="14" y2="11"/></svg>'},
];

const TOKENS = [
  ["--ds-color-bg","oklch(97% 0.012 80)"],
  ["--ds-color-surface","oklch(99% 0.005 80)"],
  ["--ds-color-surface-raised","oklch(100% 0 0)"],
  ["--ds-color-surface-overlay","oklch(97% 0.008 80)"],
  ["--ds-color-border-subtle","oklch(92% 0.012 80)"],
  ["--ds-color-border","oklch(89% 0.012 80)"],
  ["--ds-color-border-strong","oklch(82% 0.015 75)"],
  ["--ds-color-muted","oklch(48% 0.015 60)"],
  ["--ds-color-fg-subtle","oklch(35% 0.018 60)"],
  ["--ds-color-fg","oklch(20% 0.02 60)"],
  ["--ds-color-fg-strong","oklch(14% 0.025 60)"],
  ["--ds-color-fg-inverse","oklch(97% 0.005 80)"],
  ["--ds-color-white","oklch(100% 0 0)"],
  ["--ds-color-black","oklch(0% 0 0)"],
  ["--ds-color-olive-50","oklch(90% 0.025 115)"],
  ["--ds-color-olive-100","oklch(82% 0.035 115)"],
  ["--ds-color-olive-200","oklch(72% 0.05 115)"],
  ["--ds-color-olive-300","oklch(62% 0.065 115)"],
  ["--ds-color-olive-400","oklch(52% 0.08 115) ★"],
  ["--ds-color-olive-500","oklch(45% 0.085 115)"],
  ["--ds-color-olive-600","oklch(38% 0.08 115)"],
  ["--ds-color-olive-700","oklch(30% 0.07 115)"],
  ["--ds-color-olive-800","oklch(22% 0.055 115)"],
  ["--ds-color-olive-900","oklch(15% 0.04 115)"],
  ["--ds-accent","var(--ds-color-olive-400)"],
  ["--ds-accent-hover","var(--ds-color-olive-500)"],
  ["--ds-accent-soft","var(--ds-color-olive-100)"],
  ["--ds-accent-muted","var(--ds-color-olive-50)"],
  ["--ds-color-success","oklch(55% 0.1 145)"],
  ["--ds-color-success-bg","oklch(93% 0.025 145)"],
  ["--ds-color-warning","oklch(65% 0.1 85)"],
  ["--ds-color-warning-bg","oklch(95% 0.025 85)"],
  ["--ds-color-error","oklch(50% 0.14 30)"],
  ["--ds-color-error-bg","oklch(93% 0.025 30)"],
  ["--ds-color-info","oklch(55% 0.08 240)"],
  ["--ds-color-info-bg","oklch(93% 0.02 240)"],
  ["--ds-font-display","Iowan Old Style, Charter, Georgia, serif"],
  ["--ds-font-body","SF Pro, system-ui, sans-serif"],
  ["--ds-font-mono","JetBrains Mono, IBM Plex Mono, monospace"],
  ["--ds-font-ui","SF Pro, system-ui, sans-serif"],
  ["--ds-text-caption","0.75rem (12px)"],
  ["--ds-text-body-sm","0.875rem (14px)"],
  ["--ds-text-body","1rem (16px)"],
  ["--ds-text-body-lg","1.125rem (18px)"],
  ["--ds-text-lead","1.25rem (20px)"],
  ["--ds-text-h5","1.25rem (20px)"],
  ["--ds-text-h4","1.5rem (24px)"],
  ["--ds-text-h3","1.875rem (30px)"],
  ["--ds-text-h2","2.25rem (36px)"],
  ["--ds-text-h1","3rem (48px)"],
  ["--ds-text-display","3.75rem (60px)"],
  ["--ds-text-hero","4.5rem (72px)"],
  ["--ds-weight-light","300"],
  ["--ds-weight-regular","400"],
  ["--ds-weight-medium","500"],
  ["--ds-weight-semibold","600"],
  ["--ds-weight-bold","700"],
  ["--ds-leading-tight","1.1"],
  ["--ds-leading-snug","1.25"],
  ["--ds-leading-body","1.55"],
  ["--ds-leading-relaxed","1.7"],
  ["--ds-leading-loose","2"],
  ["--ds-tracking-tight","-0.01em"],
  ["--ds-tracking-normal","0.02em"],
  ["--ds-tracking-wide","0.04em"],
  ["--ds-tracking-wider","0.08em"],
  ["--ds-tracking-widest","0.12em"],
  ["--ds-space-0","0"],
  ["--ds-space-1","0.25rem (4px)"],
  ["--ds-space-2","0.5rem (8px)"],
  ["--ds-space-3","0.75rem (12px)"],
  ["--ds-space-4","1rem (16px)"],
  ["--ds-space-5","1.25rem (20px)"],
  ["--ds-space-6","1.5rem (24px)"],
  ["--ds-space-7","1.75rem (28px)"],
  ["--ds-space-8","2rem (32px)"],
  ["--ds-space-9","2.25rem (36px)"],
  ["--ds-space-10","2.5rem (40px)"],
  ["--ds-space-11","2.75rem (44px)"],
  ["--ds-space-12","3rem (48px)"],
  ["--ds-space-14","3.5rem (56px)"],
  ["--ds-space-16","4rem (64px)"],
  ["--ds-space-18","4.5rem (72px)"],
  ["--ds-space-20","5rem (80px)"],
  ["--ds-space-24","6rem (96px)"],
  ["--ds-space-28","7rem (112px)"],
  ["--ds-space-32","8rem (128px)"],
  ["--ds-radius-none","0"],
  ["--ds-radius-sm","2px"],
  ["--ds-radius-md","4px"],
  ["--ds-radius-lg","8px"],
  ["--ds-radius-xl","12px"],
  ["--ds-radius-2xl","16px"],
  ["--ds-radius-full","9999px"],
  ["--ds-shadow-xs","0 1px 2px oklch(0% 0 0 / 4%)"],
  ["--ds-shadow-sm","0 1px 3px oklch(0% 0 0 / 6%)"],
  ["--ds-shadow-md","0 4px 6px oklch(0% 0 0 / 6%)"],
  ["--ds-shadow-lg","0 10px 15px oklch(0% 0 0 / 8%)"],
  ["--ds-shadow-xl","0 20px 25px oklch(0% 0 0 / 10%)"],
  ["--ds-shadow-2xl","0 25px 50px oklch(0% 0 0 / 12%)"],
  ["--ds-shadow-inner","inset 0 2px 4px oklch(0% 0 0 / 4%)"],
  ["--ds-duration-150","150ms"],
  ["--ds-duration-200","200ms"],
  ["--ds-duration-300","300ms"],
  ["--ds-duration-500","500ms"],
  ["--ds-ease-out","cubic-bezier(0.16, 1, 0.3, 1)"],
  ["--ds-ease-spring","cubic-bezier(0.34, 1.56, 0.64, 1)"],
  ["--ds-bp-sm","640px"],
  ["--ds-bp-md","768px"],
  ["--ds-bp-lg","1024px"],
  ["--ds-bp-xl","1280px"],
  ["--ds-z-dropdown","100"],
  ["--ds-z-sticky","200"],
  ["--ds-z-overlay","300"],
  ["--ds-z-modal","400"],
  ["--ds-z-toast","500"],
  ["--ds-color-overlay","oklch(0% 0 0 / 40%)"],
  ["--ds-color-overlay-light","oklch(0% 0 0 / 12%)"],
  ["--ds-glass-bg","oklch(97% 0.012 80 / 55%)"],
  ["--ds-glass-border","oklch(89% 0.012 80 / 25%)"],
  ["--ds-glass-shadow","0 4px 24px oklch(0% 0 0 / 6%)"],
  ["--ds-blur-sm","4px"],
  ["--ds-blur-md","12px"],
  ["--ds-blur-lg","24px"],
  ["--ds-blur-xl","48px"],
];

/* ===== Init: render icon grid ===== */
(function() {
  const grid = document.getElementById("icon-grid");
  if (!grid) return;
  ICONS.forEach(function(ic) {
    const box = document.createElement("div");
    box.className = "ds-icon-box";
    box.innerHTML = ic.svg + "<span>" + ic.id + "</span>";
    box.title = ic.id;
    grid.appendChild(box);
  });
})();

/* ===== Init: render token table ===== */
(function() {
  const tb = document.getElementById("token-tbody");
  if (!tb) return;
  TOKENS.forEach(function(t) {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    td1.textContent = t[0];
    const td2 = document.createElement("td");
    td2.textContent = t[1];
    tr.appendChild(td1);
    tr.appendChild(td2);
    tb.appendChild(tr);
  });
})();

/* ===== Theme Switcher ===== */
(function() {
  const THEME_KEY = "ds-theme-mode";
  const themes = ["system", "light", "dark"];
  const labels = { system: "跟随系统", light: "浅色模式", dark: "暗色模式" };

  function getSystemPref() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(mode) {
    const html = document.documentElement;
    if (mode === "system") {
      html.setAttribute("data-theme", getSystemPref());
      html.removeAttribute("data-theme-mode");
      html.setAttribute("data-theme-mode", "system");
    } else {
      html.setAttribute("data-theme", mode);
      html.removeAttribute("data-theme-mode");
      html.setAttribute("data-theme-mode", mode);
    }
    try { localStorage.setItem(THEME_KEY, mode); } catch(e) { console.warn("[EDIC] Theme preference could not be saved (localStorage blocked)"); }
    updateButton(mode);
  }

  function updateButton(mode) {
    const btns = document.querySelectorAll(".ds-theme-toggle-btn");
    const icons = ICONS.reduce(function(acc, ic) { acc[ic.id] = ic.svg; return acc; }, {});
    Array.prototype.forEach.call(btns, function(btn) {
      if (!btn) return;
      const iconEl = btn.querySelector(".theme-icon");
      if (mode === "dark") {
        iconEl.innerHTML = icons.moon;
        btn.setAttribute("aria-label", "暗色模式 · 点击切换");
      } else if (mode === "light") {
        iconEl.innerHTML = icons.sun;
        btn.setAttribute("aria-label", "浅色模式 · 点击切换");
      } else {
        iconEl.innerHTML = icons.monitor;
        btn.setAttribute("aria-label", "跟随系统 · 点击切换");
      }
    });
  }

  function cycleTheme() {
    const mode = document.documentElement.getAttribute("data-theme-mode") || "system";
    if (mode === "light") {
      applyTheme("dark");
    } else if (mode === "dark") {
      applyTheme("system");
    } else {
      applyTheme("light");
    }
  }

  window.setTheme = function(mode) {
    if (themes.indexOf(mode) !== -1) applyTheme(mode);
  };

  window.cycleTheme = cycleTheme;

  function init() {
    let saved;
    try { saved = localStorage.getItem(THEME_KEY); } catch(e) { console.warn("[EDIC] Theme preference could not be read (localStorage blocked)"); }
    const initial = themes.indexOf(saved) !== -1 ? saved : "system";
    applyTheme(initial);

    const btns = document.querySelectorAll(".ds-theme-toggle-btn");
    Array.prototype.forEach.call(btns, function(btn) {
      if (btn) btn.addEventListener("click", cycleTheme);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function(e) {
    if (document.documentElement.getAttribute("data-theme-mode") === "system") {
      document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
    }
  });
})();

/* ===== Language Switcher ===== */
(function() {
  const LANG_KEY = "ds-lang";
  const LANGS = ["zh-CN", "en", "ja", "ko", "zh-Hant"];
  const LABELS = { "zh-CN": "中文", en: "EN", ja: "JA", ko: "KO", "zh-Hant": "繁體" };

  function applyLang(lang) {
    document.documentElement.lang = lang;
    try { localStorage.setItem(LANG_KEY, lang); } catch(e) { console.warn("[EDIC] Language preference could not be saved (localStorage blocked)"); }
    updateButtons(lang);
  }

  function updateButtons(lang) {
    var btns = document.querySelectorAll(".ds-lang-switch-btn");
    Array.prototype.forEach.call(btns, function(btn) {
      if (!btn) return;
      btn.setAttribute("aria-label", "语言：" + (LABELS[lang] || lang));
      var label = btn.querySelector(".lang-label");
      if (label) label.textContent = LABELS[lang] || lang;
    });
  }

  function cycleLang() {
    var current = document.documentElement.lang || "zh-CN";
    var idx = LANGS.indexOf(current);
    var next = LANGS[(idx + 1) % LANGS.length];
    applyLang(next);
  }

  window.setLang = function(lang) {
    if (LANGS.indexOf(lang) !== -1) applyLang(lang);
  };

  window.cycleLang = cycleLang;

  function init() {
    var saved;
    try { saved = localStorage.getItem(LANG_KEY); } catch(e) { console.warn("[EDIC] Language preference could not be read (localStorage blocked)"); }
    var initial = LANGS.indexOf(saved) !== -1 ? saved : document.documentElement.lang || "zh-CN";
    applyLang(initial);

    var btns = document.querySelectorAll(".ds-lang-switch-btn");
    Array.prototype.forEach.call(btns, function(btn) {
      if (btn) btn.addEventListener("click", cycleLang);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

/* ===== Slider sync ===== */
(function() {
  function syncSlider(slider) {
    const val = slider.value;
    const wrap = slider.parentElement;
    const fill = wrap && wrap.querySelector(".ds-slider-fill");
    const valueSpan = document.getElementById(slider.dataset.valId);
    if (fill) fill.style.width = val + "%";
    if (valueSpan) valueSpan.textContent = val + "%";
  }
  const sliders = document.querySelectorAll(".ds-slider");
  Array.prototype.forEach.call(sliders, function(slider) {
    slider.addEventListener("input", function() { syncSlider(this); });
    slider.addEventListener("change", function() { syncSlider(this); });
    syncSlider(slider);
  });
})();

/* ===== Mobile Navigation ===== */
(function() {
  const nav = document.querySelector(".ds-navbar");
  const trigger = document.getElementById("mnav-trigger");
  const panel = document.getElementById("mnav-panel");
  const backdrop = document.getElementById("mnav-backdrop");
  if (!trigger || !panel) return;

  let isOpen = false;
  let savedScrollY = 0;
  let lastFocused = null;

  function open(shouldFocusMenu) {
    if (isOpen) return;
    isOpen = true;
    lastFocused = document.activeElement;
    // Save current scroll position before locking
    savedScrollY = window.scrollY || window.pageYOffset || 0;
    // Lock background scroll with overflow:hidden instead of position:fixed
    // (position:fixed causes scroll restoration issues on some browsers)
    savedOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = "hidden";
    savedTouchAction = document.documentElement.style.touchAction;
    document.documentElement.style.touchAction = "none";
    if (nav) nav.classList.add("is-menu-open");
    panel.classList.add("is-open");
    // The drawer locks scroll, traps focus and dims the page — i.e. it behaves as a
    // modal — so expose modal semantics while open (set dynamically, never on desktop).
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-modal", "true");
    panel.setAttribute("aria-label", "导航菜单");
    // Block pointer events only on main content area, not on the navbar/menu
    const main = document.getElementById("ds-main") || document.querySelector("main");
    if (main) main.style.pointerEvents = "none";
    if (backdrop) backdrop.classList.add("is-open");
    trigger.classList.add("is-open");
    trigger.setAttribute("aria-expanded", "true");
    trigger.setAttribute("aria-label", "关闭导航菜单");
    // Only pull focus into the menu for keyboard activation (click detail === 0),
    // so pointer/touch users are not scroll-jumped.
    if (shouldFocusMenu) {
      setTimeout(function() {
        const first = panel.querySelector(".ds-navbar-link");
        if (first) first.focus();
      }, 60);
    }
  }

  function close(options) {
    if (!isOpen) return;
    const opts = options || {};
    isOpen = false;
    // Remove pointer-events block from main content
    const main = document.getElementById("ds-main") || document.querySelector("main");
    if (main) main.style.pointerEvents = "";
    // Restore body styles first (body stays in normal flow - no layout shift)
    if (savedOverflow) {
      document.documentElement.style.overflow = savedOverflow;
    } else {
      document.documentElement.style.removeProperty("overflow");
    }
    // Explicitly set touchAction to restore default behavior (not just removeProperty)
    document.documentElement.style.touchAction = savedTouchAction || "";
    // Close any open details element
    const details = panel && panel.querySelector("details[open]");
    if (details) details.removeAttribute("open");
    if (nav) nav.classList.remove("is-menu-open");
    panel.classList.remove("is-open");
    panel.removeAttribute("role");
    panel.removeAttribute("aria-modal");
    panel.removeAttribute("aria-label");
    if (backdrop) backdrop.classList.remove("is-open");
    trigger.classList.remove("is-open");
    trigger.setAttribute("aria-expanded", "false");
    trigger.setAttribute("aria-label", "打开导航菜单");
    // Body is back in normal flow now; restore the exact scroll position.
    window.scrollTo(0, savedScrollY);
    if (opts.restoreFocus !== false && lastFocused && lastFocused.focus) lastFocused.focus();
  }

  trigger.addEventListener("click", function(e) {
    e.stopPropagation();
    if (isOpen) close();
    else open(e.detail === 0);
  });
  if (backdrop) backdrop.addEventListener("click", function() { close(); });

  // When a user taps a real navigation link, let the browser handle the
  // navigation naturally. Calling close() here runs window.scrollTo() and
  // mutates document overflow/touch-action synchronously, which on mobile
  // browsers can race the navigation and abort the page load — the result
  // is the menu closes but the target page never paints. The new page
  // will fully replace the document, so there's nothing to clean up.
  // The only link that should NOT navigate is the in-page theme toggle.
  Array.prototype.forEach.call(panel.querySelectorAll(".ds-navbar-link"), function(l) {
    l.addEventListener("click", function(e) {
      // Anchor links with a real href: defer entirely to the browser.
      if (l.getAttribute("href")) return;
      // Non-anchor controls (defensive): close the menu on activation.
      if (isOpen) close({ restoreFocus: false });
    });
  });

  document.addEventListener("keydown", function(e) {
    if (!isOpen) return;
    if (e.key === "Escape") { e.preventDefault(); close(); return; }
    if (e.key === "Tab") {
      // Panel lives inside <nav>, so trapping across <nav> captures every visible
      // control (logo + trigger/X + links) and prevents focus escaping the modal.
      const scope = nav || panel;
      const els = scope.querySelectorAll('a[href], button:not([disabled])');
      if (!els.length) return;
      const first = els[0], last = els[els.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  // Auto-close when the layout crosses into the desktop breakpoint (--ds-bp-lg 1024px)
  const mq = window.matchMedia("(min-width:1024px)");
  function onResize(e) { if (e.matches && isOpen) close({ restoreFocus: false }); }
  if (mq.addEventListener) mq.addEventListener("change", onResize);
  else if (mq.addListener) mq.addListener(onResize);
  // Cleanup on page unload
  window.addEventListener("unload", function() {
    if (mq.removeEventListener) mq.removeEventListener("change", onResize);
    else if (mq.removeListener) mq.removeListener(onResize);
  });

  if (nav) {
    const onScroll = function() { nav.classList.toggle("ds-navbar--scrolled", window.scrollY > 20); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    // Cleanup on page unload
    window.addEventListener("unload", function() {
      window.removeEventListener("scroll", onScroll);
    });
  }
})();

/* ===== Page Navigation (unified TOC) controller =====
   Drives every .ds-pagenav: optional link generation from page sections,
   scroll-spy active state, smooth in-page scrolling, and mobile auto-collapse.
   Works for .ds-doc-block[id] (docs) and .ds-section[id]. */
(function() {
  const navs = document.querySelectorAll(".ds-pagenav");
  if (!navs.length) return;
  const reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const mqMobile = window.matchMedia ? window.matchMedia("(max-width: 1023px)") : null;

  Array.prototype.forEach.call(navs, function(nav) {
    const list = nav.querySelector(".ds-pagenav-list");
    if (!list) return;
    const disclosure = nav.querySelector(".ds-pagenav-disclosure");
    const isRail = nav.classList.contains("ds-pagenav--rail");

    /* Optional generation from page sections */
    const genSel = nav.getAttribute("data-pagenav-generate");
    if (genSel) {
      let n = 0;
      Array.prototype.forEach.call(document.querySelectorAll(genSel), function(sec) {
        const id = sec.getAttribute("id");
        if (!id) return;
        const header = sec.querySelector(".ds-section-header");
        const titleEl = (header || sec).querySelector("h2");
        n += 1;
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = "#" + id;
        a.className = "ds-pagenav-link";
        a.innerHTML = '<span class="ds-pagenav-num">' + (n < 10 ? "0" + n : n) + '</span><span class="ds-pagenav-text"></span>';
        a.querySelector(".ds-pagenav-text").textContent = titleEl ? titleEl.textContent.trim() : id;
        li.appendChild(a);
        list.appendChild(li);
      });
    }

    const links = Array.prototype.slice.call(list.querySelectorAll(".ds-pagenav-link"));
    if (!links.length) { nav.style.display = "none"; return; }
    const targets = links.map(function(a) {
      const href = a.getAttribute("href") || "";
      return href.charAt(0) === "#" ? document.getElementById(href.slice(1)) : null;
    });

    // Reveal the active link ONLY within the TOC's own scroll container
    // (e.g. the desktop floating rail with overflow-y:auto). Never call
    // Element.scrollIntoView here: the native API walks every scrollable
    // ancestor up to the document, so when the TOC sits in normal flow
    // (mobile disclosure / docs sidebar) it yanks the whole page back up —
    // the "异常回滚" scroll-back bug (issue #135). Adjusting scrollTop on an
    // internal scroller keeps the page scroll position untouched.
    function revealInNavScroller(linkEl) {
      let el = linkEl.parentElement;
      while (el) {
        const oy = window.getComputedStyle(el).overflowY;
        const scrollable = (oy === "auto" || oy === "scroll") && el.scrollHeight > el.clientHeight + 1;
        if (scrollable) {
          const cRect = el.getBoundingClientRect();
          const lRect = linkEl.getBoundingClientRect();
          if (lRect.top < cRect.top) {
            el.scrollTop -= (cRect.top - lRect.top) + 8;
          } else if (lRect.bottom > cRect.bottom) {
            el.scrollTop += (lRect.bottom - cRect.bottom) + 8;
          }
          return;
        }
        if (el === nav) break;
        el = el.parentElement;
      }
      // No internal scroll container → do nothing (page scroll stays put).
    }

    function setActive(id) {
      links.forEach(function(a) {
        const on = a.getAttribute("href") === "#" + id;
        a.classList.toggle("ds-pagenav-link--active", on);
        if (on) revealInNavScroller(a);
      });
      // Update aria-live region for screen reader announcement
      let liveRegion = nav.querySelector(".ds-pagenav-live");
      if (!liveRegion) {
        liveRegion = document.createElement("div");
        liveRegion.className = "ds-sr-only ds-pagenav-live";
        liveRegion.setAttribute("aria-live", "polite");
        liveRegion.setAttribute("aria-atomic", "true");
        nav.appendChild(liveRegion);
      }
      liveRegion.textContent = "";
      window.setTimeout(function() { liveRegion.textContent = "当前: " + id; }, 50);
    }

    /* Scroll-spy: highlight the topmost section in view */
    if ("IntersectionObserver" in window) {
      let debounce = null;
      const obs = new IntersectionObserver(function(entries) {
        let topId = null, topY = Infinity;
        entries.forEach(function(en) {
          if (en.isIntersecting && en.boundingClientRect.top < topY) {
            topY = en.boundingClientRect.top;
            topId = en.target.getAttribute("id");
          }
        });
        if (!topId) return;
        clearTimeout(debounce);
        debounce = setTimeout(function() { setActive(topId); }, 16);
      }, { threshold: 0, rootMargin: "-20% 0px -70% 0px" });
      targets.forEach(function(t) { if (t) obs.observe(t); });
      // Cleanup on page unload
      window.addEventListener("unload", function() { obs.disconnect(); });
    }

    // [Fix B5] Activate the first link immediately on page load — IntersectionObserver
    // only fires on scroll/resize, so without this the TOC shows nothing highlighted
    // when the page first loads or is reloaded at the top.
    if (links.length) setActive(links[0].getAttribute("href").slice(1));

    /* Rail reveal: hidden over the hero, slides in once content is reached */
    if (isRail) {
      const firstTarget = targets.find(function(t) { return !!t; });
      const updateReveal = function() {
        const past = firstTarget ? firstTarget.getBoundingClientRect().top <= 80 : true;
        nav.classList.toggle("ds-pagenav--hidden", !past);
      };
      if ("IntersectionObserver" in window) {
        window.addEventListener("scroll", updateReveal, { passive: true });
        updateReveal();
      } else {
        nav.classList.remove("ds-pagenav--hidden");
      }
    }

    /* Smooth in-page scroll + close the disclosure on mobile after picking */
    links.forEach(function(a) {
      a.addEventListener("click", function(e) {
        const href = this.getAttribute("href") || "";
        if (href.charAt(0) !== "#") return;
        const target = document.getElementById(href.slice(1));
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
        if (!reduceMotion && window.history && history.replaceState) {
          history.replaceState(null, "", href);
        }
        if (disclosure && disclosure.hasAttribute("open") && mqMobile && mqMobile.matches) {
          disclosure.removeAttribute("open");
        }
      });
    });
  });
})();


/* =========================================================================
   EDIC Design System v1.1 — Site interactions
   Scroll reveal · Copy to clipboard · Tabs · Accordion · Docs nav · Year
   All blocks are self-guarding; safe to load on every page.
   ========================================================================= */

/* ===== Scroll reveal ===== */
(function() {
  const els = document.querySelectorAll(".ds-reveal");
  if (!els.length) return;
  const reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(els, function(el) { el.classList.add("is-visible"); });
    return;
  }
  const obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  Array.prototype.forEach.call(els, function(el) { obs.observe(el); });
  // Cleanup on page unload to prevent memory leaks
  window.addEventListener("unload", function() { obs.disconnect(); });
})();

/* ===== Copy to clipboard ===== */
(function() {
  function copyText(text) {
    return navigator.clipboard.writeText(text);
  }

  function getSourceText(btn) {
    if (btn.hasAttribute("data-copy-text")) return btn.getAttribute("data-copy-text");
    const sel = btn.getAttribute("data-copy");
    if (!sel) return "";
    const src = document.querySelector(sel);
    if (!src) return "";
    if (src.value !== undefined && (src.tagName === "TEXTAREA" || src.tagName === "INPUT")) return src.value;
    return src.innerText || src.textContent || "";
  }

  document.addEventListener("click", function(e) {
    const btn = e.target.closest ? e.target.closest("[data-copy],[data-copy-text]") : null;
    if (!btn) return;
    e.preventDefault();
    const text = getSourceText(btn);
    if (!text) return;
    // [Fix B3] Hoist label and original before .then()/.catch() split so both
    // branches can reference them. Previously original was declared only inside
    // .then(), causing a ReferenceError in .catch() that silently stopped the
    // error-state timeout — the button stayed stuck on "复制失败" forever.
    const label = btn.querySelector(".ds-copy-label");
    const original = label ? label.textContent : btn.getAttribute("data-label-original") || btn.textContent.trim();
    if (!label && !btn.getAttribute("data-label-original")) btn.setAttribute("data-label-original", btn.textContent.trim());
    copyText(text).then(function() {
      btn.classList.add("is-copied");
      const copiedText = label ? (btn.dataset.copiedLabel || "已复制") : "已复制";
      if (label) { label.textContent = copiedText; }
      else { btn.setAttribute("data-was", btn.innerHTML); }
      window.setTimeout(function() {
        btn.classList.remove("is-copied");
        if (label && original) label.textContent = original;
      }, 1800);
    }).catch(function() {
      // Show error state on button
      if (label) label.textContent = "复制失败";
      btn.classList.add("is-error");
      window.setTimeout(function() {
        btn.classList.remove("is-error");
        if (label && original) label.textContent = original;
      }, 2000);
    });
  });
})();

/* ===== Functional tabs ===== */
(function() {
  const groups = document.querySelectorAll("[data-tabs]");
  if (!groups.length) return;
  Array.prototype.forEach.call(groups, function(group) {
    // [Fix B7] WAI-ARIA Tabs pattern: role=tablist on container
    group.setAttribute("role", "tablist");

    const tabs = Array.prototype.slice.call(group.querySelectorAll("[data-tab]"));
    const scope = group.getAttribute("data-tabs-scope");
    const panelHost = scope ? document.querySelector(scope) : group.parentNode;

    function activate(name) {
      Array.prototype.forEach.call(tabs, function(t) {
        const on = t.getAttribute("data-tab") === name;
        t.classList.toggle("ds-tab--active", on);
        t.setAttribute("aria-selected", on ? "true" : "false");
        // [Fix B7] Roving tabindex: only active tab in tab order
        t.setAttribute("tabindex", on ? "0" : "-1");
      });
      const panels = (panelHost || document).querySelectorAll("[data-panel]");
      Array.prototype.forEach.call(panels, function(p) {
        p.classList.toggle("is-active", p.getAttribute("data-panel") === name);
      });
    }

    // [Fix B7] role=tabpanel on every panel
    const allPanels = (panelHost || document).querySelectorAll("[data-panel]");
    Array.prototype.forEach.call(allPanels, function(p) {
      p.setAttribute("role", "tabpanel");
    });

    Array.prototype.forEach.call(tabs, function(t, idx) {
      // [Fix B7] role=tab on every tab button
      t.setAttribute("role", "tab");

      t.addEventListener("click", function() { activate(this.getAttribute("data-tab")); });
      t.addEventListener("keydown", function(e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          activate(this.getAttribute("data-tab"));
          return;
        }
        // [Fix B7] Arrow key navigation (WAI-ARIA Tabs pattern)
        if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
          e.preventDefault();
          const dir = e.key === "ArrowRight" ? 1 : -1;
          const next = (idx + dir + tabs.length) % tabs.length;
          tabs[next].focus();
        }
      });
    });

    const first = tabs[0];
    if (first) activate(first.getAttribute("data-tab"));
  });
})();

/* ===== Accordion ===== */
(function() {
  const headers = document.querySelectorAll(".ds-accordion-header");
  if (!headers.length) return;
  Array.prototype.forEach.call(headers, function(h) {
    // [Fix B2] Accordion headers are <div> elements. Without role=button and
    // tabindex=0 the Tab key skips them entirely and screen readers don't
    // announce them as interactive. JS injects both attributes at init.
    h.setAttribute("role", "button");
    h.setAttribute("tabindex", "0");

    // Initialize ARIA attributes on first load
    const item = h.closest(".ds-accordion-item");
    if (item) {
      const panel = item.querySelector(".ds-accordion-content");
      const panelId = panel ? panel.id || (panel.id = "ds-accordion-panel-" + Math.random().toString(36).slice(2)) : null;
      h.setAttribute("aria-expanded", item.classList.contains("open") ? "true" : "false");
      if (panel) panel.setAttribute("aria-hidden", item.classList.contains("open") ? "false" : "true");
      if (panelId) h.setAttribute("aria-controls", panelId);
    }

    function toggleAccordion(header) {
      const item = header.closest(".ds-accordion-item");
      if (!item) return;
      const isOpen = item.classList.toggle("open");
      header.setAttribute("aria-expanded", String(isOpen));
      const panel = item.querySelector(".ds-accordion-content");
      if (panel) panel.setAttribute("aria-hidden", String(!isOpen));
    }

    h.addEventListener("click", function() { toggleAccordion(this); });
    // Keyboard activation: Enter and Space
    h.addEventListener("keydown", function(e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggleAccordion(this);
      }
    });
  });
})();

/* ===== Current year stamp ===== */
(function() {
  const year = String(new Date().getFullYear());
  const els = document.querySelectorAll(".ds-year");
  Array.prototype.forEach.call(els, function(el) { el.textContent = year; });
})();


/* ===== Tooltip ===== */
(function() {
  var tooltipWrappers = document.querySelectorAll("[data-tooltip]");
  if (!tooltipWrappers.length) return;

  function showTooltip(wrapper) {
    var tooltip = wrapper._tooltip;
    if (!tooltip) {
      var id = "ds-tooltip-" + Math.random().toString(36).slice(2);
      tooltip = document.createElement("span");
      tooltip.className = "ds-tooltip";
      tooltip.id = id;
      tooltip.setAttribute("role", "tooltip");
      tooltip.textContent = wrapper.getAttribute("data-tooltip");
      wrapper.appendChild(tooltip);
      wrapper._tooltip = tooltip;
      wrapper.setAttribute("aria-describedby", id);
    }
    // eslint-disable-next-line no-unused-expressions
    tooltip.offsetHeight;
    tooltip.style.opacity = "1";
    tooltip.setAttribute("aria-hidden", "false");
  }

  function hideTooltip(wrapper) {
    var tooltip = wrapper._tooltip;
    if (tooltip) {
      tooltip.style.opacity = "0";
      tooltip.setAttribute("aria-hidden", "true");
    }
  }

  Array.prototype.forEach.call(tooltipWrappers, function(wrapper) {
    
    wrapper.classList.add("ds-tooltip-host");
    wrapper.setAttribute("tabindex", "0");

    wrapper.addEventListener("mouseenter", function() { showTooltip(this); });
    wrapper.addEventListener("mouseleave", function() { hideTooltip(this); });
    wrapper.addEventListener("focus", function() { showTooltip(this); });
    wrapper.addEventListener("blur", function() { hideTooltip(this); });
  });
})();
/* ===== Toast auto-dismiss functionality ===== */
(function() {
  // Auto-dismiss toast notifications after 5 seconds
  var toastElements = document.querySelectorAll('.ds-toast');
  
  Array.prototype.forEach.call(toastElements, function(toast) {
    // Skip if already has auto-dismiss data attribute set
    if (toast.hasAttribute('data-auto-dismiss')) {
      var dismissDelay = parseInt(toast.getAttribute('data-auto-dismiss'), 10);
      if (isNaN(dismissDelay) || dismissDelay < 0) {
        dismissDelay = 5000; // default 5 seconds
      }
      if (dismissDelay > 0) {
        setTimeout(function() {
          dismissToast(toast);
        }, dismissDelay);
      }
    } else {
      // Default auto-dismiss after 5 seconds for all toasts
      setTimeout(function() {
        dismissToast(toast);
      }, 5000);
    }
    
    // Add click handler for close button
    var closeBtn = toast.querySelector('.ds-toast-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', function() {
        dismissToast(toast);
      });
    }
  });
  
  function dismissToast(toast) {
    // Check if already dismissing
    if (toast.classList.contains('ds-toast-dismissing')) {
      return;
    }
    
    // Add dismissing class to trigger CSS transition
    toast.classList.add('ds-toast-dismissing');
    
    // Remove from DOM after animation completes
    setTimeout(function() {
      if (toast.parentNode) {
        toast.parentNode.removeChild(toast);
      }
    }, 300); // Match CSS transition duration
  }
})();
