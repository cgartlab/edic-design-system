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
      // P1-2: 系统主题变化时同步更新按钮图标/aria-label
      updateButton("system");
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
  let savedOverflow, savedTouchAction;

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
      // P2-7: 修正条件反转 — 支持 IO 时优先用 IO（无 reflow），不支持时回退 scroll 事件
      if ("IntersectionObserver" in window && firstTarget) {
        const railObs = new IntersectionObserver(function(entries) {
          nav.classList.toggle("ds-pagenav--hidden", !entries[0].isIntersecting);
        }, { threshold: 0, rootMargin: "-80px 0px 0px 0px" });
        railObs.observe(firstTarget);
        window.addEventListener("unload", function() { railObs.disconnect(); });
      } else {
        // Fallback: scroll + getBoundingClientRect（无 IO 时使用）
        window.addEventListener("scroll", updateReveal, { passive: true });
        updateReveal();
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
  // S-4: 递增计数器生成面板 ID，避免 Math.random 非确定
  var panelCounter = 0;
  Array.prototype.forEach.call(headers, function(h) {
    // [Fix B2] Accordion headers are <div> elements. Without role=button and
    // tabindex=0 the Tab key skips them entirely and screen readers don't
    // announce them as interactive. JS injects both attributes at init.
    h.setAttribute("role", "button");
    h.setAttribute("tabindex", "0");

    // P2-3: 以 DOM 内联 aria 属性为准；若 HTML 已声明则不覆盖
    const item = h.closest(".ds-accordion-item");
    if (item) {
      const panel = item.querySelector(".ds-accordion-content");
      // S-4: 递增计数器命名
      var panelId = null;
      if (panel) {
        if (panel.id) {
          panelId = panel.id;
        } else {
          panelCounter++;
          panel.id = "ds-accordion-panel-" + panelCounter;
          panelId = panel.id;
        }
      }
      // P2-3: 优先读取 HTML 已有的 aria-expanded，否则从 class 推导
      if (!h.hasAttribute("aria-expanded")) {
        h.setAttribute("aria-expanded", item.classList.contains("open") ? "true" : "false");
      }
      if (panel && !panel.hasAttribute("aria-hidden")) {
        panel.setAttribute("aria-hidden", item.classList.contains("open") ? "false" : "true");
      }
      if (panelId && !h.hasAttribute("aria-controls")) {
        h.setAttribute("aria-controls", panelId);
      }
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
    // P1-2: 键盘处理 — Enter/Space 切换 + 方向键/Home/End 焦点移动（WAI-ARIA Accordion Pattern）
    h.addEventListener("keydown", function(e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggleAccordion(this);
        return;
      }
      // 方向键导航：在当前 accordion 组件内的所有 header 间移动
      var container = this.closest(".ds-accordion");
      if (!container) return;
      var allHeaders = container.querySelectorAll(".ds-accordion-header");
      var idx = Array.prototype.indexOf.call(allHeaders, this);
      if (idx === -1) return;
      if (e.key === "ArrowDown") {
        e.preventDefault();
        var next = allHeaders[(idx + 1) % allHeaders.length];
        next.focus();
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        var prev = allHeaders[(idx - 1 + allHeaders.length) % allHeaders.length];
        prev.focus();
      } else if (e.key === "Home") {
        e.preventDefault();
        allHeaders[0].focus();
      } else if (e.key === "End") {
        e.preventDefault();
        allHeaders[allHeaders.length - 1].focus();
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

/* ===== Unified SVG Chart Engine ===== */
(function () {
  'use strict';
  var SVG_NS = 'http://www.w3.org/2000/svg';
  var BAR_WIDTH_RATIO = 0.5;
  var BAR_MIN_WIDTH = 14;
  var BAR_MAX_WIDTH = 64;
  var charts = document.querySelectorAll('[data-chart]');
  if (!charts.length) return;

  var COLOR_DEFAULTS = [
    'var(--ds-chart-1)', 'var(--ds-chart-2)', 'var(--ds-chart-3)',
    'var(--ds-chart-4)', 'var(--ds-chart-5)', 'var(--ds-chart-6)',
    'var(--ds-chart-7)', 'var(--ds-chart-8)'
  ];

  /* ---------- SVG element factory ---------- */
  function el(tag, attrs, parent) {
    var node = document.createElementNS(SVG_NS, tag);
    if (attrs) {
      for (var k in attrs) {
        if (!attrs.hasOwnProperty(k)) continue;
        if (k === 'class') node.setAttribute('class', attrs[k]);
        else node.setAttribute(k, attrs[k]);
      }
    }
    if (parent) parent.appendChild(node);
    return node;
  }

  /* ---------- Backward-compat config normalizer ---------- */
  function normalizeConfig(raw) {
    var cfg = raw || {};
    cfg.options = cfg.options || {};
    var o = cfg.options;
    o.colors = o.colors || [];
    if (cfg.color && o.colors.indexOf(cfg.color) === -1) o.colors.unshift(cfg.color);

    // area → line + fill
    if (cfg.type === 'area') { cfg.type = 'line'; o.fill = true; }

    // old combo top-level bar/line → series
    if (cfg.type === 'combo' && !cfg.series && (cfg.bar || cfg.line)) {
      cfg.series = [];
      if (cfg.bar) cfg.series.push({ name: 'Bar', data: cfg.bar, color: cfg.barColor || o.colors[0] || COLOR_DEFAULTS[0], chartType: 'bar' });
      if (cfg.line) cfg.series.push({ name: 'Line', data: cfg.line, color: cfg.lineColor || o.colors[1] || COLOR_DEFAULTS[1], chartType: 'line' });
    }

    // old multiline: keep series; ensure each has a color
    if ((cfg.type === 'multiline' || cfg.type === 'combo' || cfg.type === 'donut') && cfg.series) {
      for (var i = 0; i < cfg.series.length; i++) {
        var s = cfg.series[i];
        if (!s.color) s.color = o.colors[i] || COLOR_DEFAULTS[i % COLOR_DEFAULTS.length];
        if (!s.chartType) s.chartType = (cfg.type === 'combo') ? (i === 0 ? 'bar' : 'line') : 'line';
      }
    }

    // single-series (bar/hbar/line/pie/donut data) → normalize single color
    if (!cfg.series) {
      cfg._singleColor = o.colors[0] || COLOR_DEFAULTS[0];
    }

    o.height = o.height || (cfg.type === 'sparkline' ? 28 : 250);
    o.animate = o.animate !== false;
    o.tooltip = o.tooltip !== false;
    o.legend = o.legend === true;
    o.grid = o.grid !== false;
    o.gridLines = o.gridLines || 4;
    o.donutHole = o.donutHole != null ? o.donutHole : 0.55;

    // Unified axis defaults
    o.xAxis = o.xAxis || {};
    o.xAxis.show = o.xAxis.show !== false;
    o.xAxis.title = o.xAxis.title || '';
    o.xAxis.ticks = (typeof o.xAxis.ticks === 'number' && o.xAxis.ticks > 0) ? o.xAxis.ticks : 4;
    o.xAxis.format = o.xAxis.format || 'auto';
    o.yAxis = o.yAxis || {};
    o.yAxis.show = o.yAxis.show !== false;
    o.yAxis.title = o.yAxis.title || '';
    o.yAxis.ticks = (typeof o.yAxis.ticks === 'number' && o.yAxis.ticks > 0) ? o.yAxis.ticks : 4;
    o.yAxis.format = o.yAxis.format || 'auto';
    o.yAxis.min = o.yAxis.min != null ? o.yAxis.min : (o.yMin != null ? o.yMin : 'auto');
    o.yAxis.max = o.yAxis.max != null ? o.yAxis.max : (o.yMax != null ? o.yMax : 'auto');
    o.startAngle = o.startAngle != null ? o.startAngle : -90;
    o.fill = !!o.fill;
    o.dots = !!o.dots;
    o.showValues = !!o.showValues;

    // default labels for indexed data
    if (!cfg.labels && cfg.data) {
      cfg.labels = [];
      for (var j = 0; j < cfg.data.length; j++) cfg.labels.push(String(j + 1));
    }

    return cfg;
  }

  /* ---------- Context (viewBox dimensions) ---------- */
  function makeCtx(cfg) {
    var type = cfg.type, o = cfg.options;
    var h = o.height;
    var w = 500; // logical viewBox width; scales via CSS
    // Pie/donut must use a square viewBox so circles stay circular
    // (preserveAspectRatio="none" would otherwise stretch them into ellipses).
    if (type === 'pie' || type === 'donut') { w = 200; h = 200; }
    var pad;
    if (type === 'sparkline') { w = 120; h = o.height || 28; pad = 0; }
    else if (type === 'pie' || type === 'donut') pad = 8;
    else if (type === 'hbar') pad = { top: 12, right: 40, bottom: 54, left: 88 };
    else pad = { top: 12, right: 12, bottom: 54, left: 52 };
    var padT = typeof pad === 'number' ? pad : pad.top;
    var padR = typeof pad === 'number' ? pad : pad.right;
    var padB = typeof pad === 'number' ? pad : pad.bottom;
    var padL = typeof pad === 'number' ? pad : pad.left;
    return {
      w: w, h: h,
      padT: padT, padR: padR, padB: padB, padL: padL,
      plotW: w - padL - padR,
      plotH: h - padT - padB
    };
  }

  /* ---------- Scales ---------- */
  function scaleLinear(domMin, domMax, rMin, rMax) {
    var d = domMax - domMin;
    if (d === 0) d = 1;
    return function (v) { return rMin + ((v - domMin) / d) * (rMax - rMin); };
  }
  function scaleBand(count, rMin, rMax, padding) {
    var p = padding != null ? padding : 0.2;
    var step = (rMax - rMin) / count;
    var bw = step * (1 - p);
    return function (i) { return rMin + i * step + (step - bw) / 2; };
  }

  /* ---------- Bar width clamp ---------- */
  function clampBarWidth(step) {
    var w = step * BAR_WIDTH_RATIO;
    if (w < BAR_MIN_WIDTH) return BAR_MIN_WIDTH;
    if (w > BAR_MAX_WIDTH) return BAR_MAX_WIDTH;
    return w;
  }

  /* ---------- Tick helpers ---------- */
  function niceTicks(min, max, targetCount) {
    if (typeof targetCount !== 'number' || targetCount <= 0) targetCount = 4;
    var rawStep = (max - min) / targetCount;
    if (rawStep <= 0) rawStep = 1;
    var mag = Math.pow(10, Math.floor(Math.log(rawStep) / Math.LN10));
    var norm = rawStep / mag;
    var niceStep;
    if (norm < 1.5) niceStep = 1 * mag;
    else if (norm < 3.5) niceStep = 2 * mag;
    else if (norm < 7.5) niceStep = 5 * mag;
    else niceStep = 10 * mag;
    var start = Math.ceil(min / niceStep) * niceStep;
    var ticks = [];
    var maxTicks = 20; // safety cap against pathological domains
    for (var v = start; v <= max + niceStep * 0.001 && ticks.length < maxTicks; v += niceStep) {
      ticks.push(Math.round(v * 1000) / 1000);
    }
    return ticks;
  }
  function formatTick(v, format) {
    if (format === 'percent') return v + '%';
    if (Math.abs(v) >= 1000000) return (v / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
    if (Math.abs(v) >= 1000) return (v / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    if (Math.round(v) === v) return String(v);
    return v.toFixed(2).replace(/\.?0+$/, '');
  }

  /* ---------- Shared: drawAxes (replaces drawGrid + drawXLabels) ---------- */
  function drawAxes(svg, ctx, cfg, scales) {
    // scales = { x, y, xType: 'band'|'linear', yType: 'linear'|'band' }
    var o = cfg.options;
    var xCfg = o.xAxis || {}, yCfg = o.yAxis || {};
    var axisGroup = el('g', { 'class': 'ds-chart__axes' }, svg);

    // --- Y axis (left) ---
    if (yCfg.show !== false) {
      var yg = el('g', { 'class': 'ds-chart__y-axis' }, axisGroup);
      el('line', { 'class': 'ds-chart__axis-line', x1: ctx.padL, y1: ctx.padT, x2: ctx.padL, y2: ctx.h - ctx.padB }, yg);
      if (scales.yType === 'linear') {
        var yMin = scales.y._min, yMax = scales.y._max;
        var ticks = niceTicks(yMin, yMax, yCfg.ticks || 4);
        for (var i = 0; i < ticks.length; i++) {
          var ty = scales.y(ticks[i]);
          var tk = el('g', { 'class': 'ds-chart__tick' }, yg);
          el('line', { 'class': 'ds-chart__tick-line', x1: ctx.padL - 4, y1: ty.toFixed(1), x2: ctx.padL, y2: ty.toFixed(1) }, tk);
          var lb = el('text', { 'class': 'ds-chart__tick-label ds-chart__axis-label', x: ctx.padL - 15, y: ty.toFixed(1), 'text-anchor': 'end', 'dominant-baseline': 'middle' }, tk);
          lb.textContent = formatTick(ticks[i], yCfg.format);
        }
      } else if (scales.yType === 'band') {
        var labels = cfg.labels || [];
        var count = labels.length || cfg.data.length || 1;
        var stepY = ctx.plotH / count;
        for (var b = 0; b < count; b++) {
          var by = ctx.padT + (b + 0.5) * stepY;
          var tkg = el('g', { 'class': 'ds-chart__tick' }, yg);
          el('line', { 'class': 'ds-chart__tick-line', x1: ctx.padL - 4, y1: by.toFixed(1), x2: ctx.padL, y2: by.toFixed(1) }, tkg);
          if (labels[b] != null) {
            var tlb = el('text', { 'class': 'ds-chart__tick-label ds-chart__axis-label', x: ctx.padL - 15, y: by.toFixed(1), 'text-anchor': 'end', 'dominant-baseline': 'middle' }, tkg);
            tlb.textContent = labels[b];
          }
        }
      }
      if (yCfg.title) {
        var yt = el('text', { 'class': 'ds-chart__axis-title ds-chart__axis-title--y', x: -(ctx.h / 2), y: 20, transform: 'rotate(-90)', 'text-anchor': 'middle' }, yg);
        yt.textContent = yCfg.title;
      }
    }

    // --- X axis (bottom) ---
    if (xCfg.show !== false) {
      var xg = el('g', { 'class': 'ds-chart__x-axis' }, axisGroup);
      el('line', { 'class': 'ds-chart__axis-line', x1: ctx.padL, y1: ctx.h - ctx.padB, x2: ctx.w - ctx.padR, y2: ctx.h - ctx.padB }, xg);
      if (scales.xType === 'band') {
        var xLabels = cfg.labels || [];
        var xCount = xLabels.length || cfg.data.length || 1;
        var stepX = ctx.plotW / xCount;
        for (var xb = 0; xb < xCount; xb++) {
          var bx = ctx.padL + (xb + 0.5) * stepX;
          var xtkg = el('g', { 'class': 'ds-chart__tick' }, xg);
          el('line', { 'class': 'ds-chart__tick-line', x1: bx.toFixed(1), y1: ctx.h - ctx.padB, x2: bx.toFixed(1), y2: ctx.h - ctx.padB + 4 }, xtkg);
          if (xLabels[xb] != null) {
            var xtlb = el('text', { 'class': 'ds-chart__tick-label ds-chart__tick-label--x ds-chart__axis-label', x: bx.toFixed(1), y: ctx.h - ctx.padB + 18, 'text-anchor': 'middle', 'dominant-baseline': 'middle' }, xtkg);
            xtlb.textContent = xLabels[xb];
          }
        }
      } else if (scales.xType === 'linear') {
        var xMin = scales.x._min, xMax = scales.x._max;
        var xTicks = niceTicks(xMin, xMax, xCfg.ticks || 4);
        for (var t = 0; t < xTicks.length; t++) {
          var tx = scales.x(xTicks[t]);
          var tg = el('g', { 'class': 'ds-chart__tick' }, xg);
          el('line', { 'class': 'ds-chart__tick-line', x1: tx.toFixed(1), y1: ctx.h - ctx.padB, x2: tx.toFixed(1), y2: ctx.h - ctx.padB + 4 }, tg);
          var tlb2 = el('text', { 'class': 'ds-chart__tick-label ds-chart__tick-label--x ds-chart__axis-label', x: tx.toFixed(1), y: ctx.h - ctx.padB + 18, 'text-anchor': 'middle', 'dominant-baseline': 'middle' }, tg);
          tlb2.textContent = formatTick(xTicks[t], xCfg.format);
        }
      }
      if (xCfg.title) {
        var xt = el('text', { 'class': 'ds-chart__axis-title ds-chart__axis-title--x', x: ctx.w / 2, y: ctx.h - ctx.padB + 52, 'text-anchor': 'middle' }, xg);
        xt.textContent = xCfg.title;
      }
    }

    // --- Grid lines ---
    if (o.grid !== false && scales.yType === 'linear') {
      var gg = el('g', { 'class': 'ds-chart__grid' }, axisGroup);
      var yMin2 = scales.y._min, yMax2 = scales.y._max;
      var gridTicks = niceTicks(yMin2, yMax2, o.gridLines || 3);
      for (var g2 = 0; g2 < gridTicks.length; g2++) {
        var gy = scales.y(gridTicks[g2]);
        if (Math.abs(gy - (ctx.h - ctx.padB)) < 2) continue; // skip baseline
        el('line', { 'class': 'ds-chart__grid-line', x1: ctx.padL, y1: gy.toFixed(1), x2: ctx.w - ctx.padR, y2: gy.toFixed(1) }, gg);
      }
    } else if (o.grid !== false && scales.yType === 'band' && scales.xType === 'linear') {
      // HBar: vertical grid lines aligned with X (linear) ticks
      var vgg = el('g', { 'class': 'ds-chart__grid' }, axisGroup);
      var xMin2 = scales.x._min, xMax2 = scales.x._max;
      var xGridTicks = niceTicks(xMin2, xMax2, o.gridLines || 3);
      for (var g3 = 0; g3 < xGridTicks.length; g3++) {
        var gx = scales.x(xGridTicks[g3]);
        if (Math.abs(gx - ctx.padL) < 2) continue; // skip baseline
        el('line', { 'class': 'ds-chart__grid-line', x1: gx.toFixed(1), y1: ctx.padT, x2: gx.toFixed(1), y2: ctx.h - ctx.padB }, vgg);
      }
    }
    return axisGroup;
  }

  /* ---------- Renderer: Bar (vertical) ---------- */
  function renderBar(svg, cfg, ctx) {
    var data = cfg.data || [];
    var labels = cfg.labels || [];
    var color = cfg._singleColor;
    var yMin = 0;
    var yMax = -Infinity;
    for (var i = 0; i < data.length; i++) { if (data[i] > yMax) yMax = data[i]; }
    if (yMax <= 0) yMax = 1;
    var yScale = scaleLinear(yMin, yMax, ctx.h - ctx.padB, ctx.padT);
    yScale._min = yMin; yScale._max = yMax;
    var xBand = scaleBand(data.length, ctx.padL, ctx.w - ctx.padR, 0.25);
    var stepX = ctx.plotW / data.length;
    var bw = clampBarWidth(stepX);

    drawAxes(svg, ctx, cfg, { x: xBand, y: yScale, xType: 'band', yType: 'linear' });

    var g = el('g', { 'class': 'ds-chart__bars' }, svg);
    var items = [];
    for (var j = 0; j < data.length; j++) {
      var v = data[j];
      var y = yScale(Math.max(v, 0));
      var h = (ctx.h - ctx.padB) - y;
      if (h < 0) h = 0;
      var bx = ctx.padL + (j + 0.5) * stepX - bw / 2;
      var r = el('rect', {
        'class': 'ds-chart__bar',
        x: bx.toFixed(1),
        y: y.toFixed(1),
        width: bw.toFixed(1),
        height: h.toFixed(1),
        tabindex: '0',
        'data-index': j,
        'data-value': v,
        'data-label': labels[j] || '',
        role: 'img',
        'aria-label': (labels[j] || '') ? (labels[j] + ': ' + v) : String(v)
      }, g);
      r.style.setProperty('--color', color);
      if (cfg.options.animate) r.style.setProperty('--d', (j * 40) + 'ms');
      items.push(r);
    }
    return { items: items, meta: { xBand: xBand, bw: bw, yScale: yScale } };
  }

  /* ---------- Renderer: Horizontal Bar ---------- */
  function renderHBar(svg, cfg, ctx) {
    var data = cfg.data || [];
    var labels = cfg.labels || [];
    var color = cfg._singleColor;
    var xMax = -Infinity;
    for (var i = 0; i < data.length; i++) { if (data[i] > xMax) xMax = data[i]; }
    if (xMax <= 0) xMax = 1;
    var xScale = scaleLinear(0, xMax, ctx.padL, ctx.w - ctx.padR);
    xScale._min = 0; xScale._max = xMax;
    var yBand = scaleBand(data.length, ctx.padT, ctx.h - ctx.padB, 0.25);
    var stepY = ctx.plotH / data.length;
    var bh = clampBarWidth(stepY);

    drawAxes(svg, ctx, cfg, { x: xScale, y: yBand, xType: 'linear', yType: 'band' });

    var g = el('g', { 'class': 'ds-chart__hbars' }, svg);
    var items = [];
    for (var j = 0; j < data.length; j++) {
      var v = data[j];
      var w = xScale(v) - ctx.padL;
      if (w < 0) w = 0;
      var by = ctx.padT + (j + 0.5) * stepY - bh / 2;
      var r = el('rect', {
        'class': 'ds-chart__bar',
        x: ctx.padL,
        y: by.toFixed(1),
        width: w.toFixed(1),
        height: bh.toFixed(1),
        tabindex: '0',
        'data-index': j,
        'data-value': v,
        'data-label': labels[j] || '',
        role: 'img',
        'aria-label': (labels[j] || '') ? (labels[j] + ': ' + v) : String(v)
      }, g);
      r.style.setProperty('--color', color);
      if (cfg.options.animate) r.style.setProperty('--d', (j * 40) + 'ms');
      items.push(r);
    }
    return { items: items, meta: { yBand: yBand, bh: bh, xScale: xScale } };
  }

  /* ---------- Renderer: Stacked Bar ---------- */
  function renderStacked(svg, cfg, ctx) {
    var series = cfg.series || [];
    var labels = cfg.labels || [];
    var n = series.length ? series[0].data.length : 0;
    var totals = [];
    for (var i = 0; i < n; i++) {
      var t = 0;
      for (var s = 0; s < series.length; s++) t += (series[s].data[i] || 0);
      totals.push(t);
    }
    var yMax = -Infinity;
    for (var j = 0; j < totals.length; j++) { if (totals[j] > yMax) yMax = totals[j]; }
    if (yMax <= 0) yMax = 1;
    var yScale = scaleLinear(0, yMax, ctx.h - ctx.padB, ctx.padT);
    yScale._min = 0; yScale._max = yMax;
    var xBand = scaleBand(n, ctx.padL, ctx.w - ctx.padR, 0.25);
    var stepX = ctx.plotW / n;
    var bw = clampBarWidth(stepX);

    drawAxes(svg, ctx, cfg, { x: xBand, y: yScale, xType: 'band', yType: 'linear' });

    var g = el('g', { 'class': 'ds-chart__stacked' }, svg);
    var items = [];
    var cums = [];
    for (var k = 0; k < n; k++) cums.push(0);
    for (var si = 0; si < series.length; si++) {
      var sc = series[si].color;
      for (var di = 0; di < series[si].data.length; di++) {
        var v = series[si].data[di] || 0;
        var baseY = yScale(cums[di]);
        var topY = yScale(cums[di] + v);
        var h = baseY - topY;
        if (h < 0) h = 0;
        var r = el('rect', {
          'class': 'ds-chart__bar ds-chart__bar--stacked',
          x: (ctx.padL + (di + 0.5) * stepX - bw / 2).toFixed(1),
          y: topY.toFixed(1),
          width: bw.toFixed(1),
          height: h.toFixed(1),
          tabindex: '0',
          'data-index': di,
          'data-series': si,
          'data-value': v,
          'data-label': labels[di] || '',
          'data-series-name': series[si].name || '',
          role: 'img',
          'aria-label': (labels[di] || '') ? (labels[di] + ': ' + v) : String(v)
        }, g);
        r.style.setProperty('--color', sc);
        if (cfg.options.animate) r.style.setProperty('--d', (di * 40) + 'ms');
        items.push(r);
        cums[di] += v;
      }
    }
    return { items: items, meta: { xBand: xBand, bw: bw, yScale: yScale, series: series } };
  }

  /* ---------- Shared: pie arc path ---------- */
  function arcPath(cx, cy, rOuter, rInner, startA, endA) {
    var sr = startA * Math.PI / 180;
    var er = endA * Math.PI / 180;
    var sx = cx + rOuter * Math.cos(sr), sy = cy + rOuter * Math.sin(sr);
    var ex = cx + rOuter * Math.cos(er), ey = cy + rOuter * Math.sin(er);
    var large = (endA - startA) > 180 ? 1 : 0;
    if (rInner > 0) {
      var isx = cx + rInner * Math.cos(er), isy = cy + rInner * Math.sin(er);
      var iex = cx + rInner * Math.cos(sr), iey = cy + rInner * Math.sin(sr);
      return [
        'M', sx.toFixed(2), sy.toFixed(2),
        'A', rOuter.toFixed(2), rOuter.toFixed(2), 0, large, 1, ex.toFixed(2), ey.toFixed(2),
        'L', isx.toFixed(2), isy.toFixed(2),
        'A', rInner.toFixed(2), rInner.toFixed(2), 0, large, 0, iex.toFixed(2), iey.toFixed(2),
        'Z'
      ].join(' ');
    } else {
      return [
        'M', cx, cy,
        'L', sx.toFixed(2), sy.toFixed(2),
        'A', rOuter.toFixed(2), rOuter.toFixed(2), 0, large, 1, ex.toFixed(2), ey.toFixed(2),
        'Z'
      ].join(' ');
    }
  }

  /* ---------- Renderer: Pie ---------- */
  function renderPie(svg, cfg, ctx) {
    // P1-5: 饼图必须保持比例，避免拉伸为椭圆（与 multi-donut 一致）
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    var data = cfg.data || [];
    // P1-4: 空数据守卫
    if (!data.length) return { items: [], meta: {} };
    var labels = cfg.labels || [];
    var colors = cfg.options.colors.length ? cfg.options.colors : COLOR_DEFAULTS;
    var total = 0;
    for (var i = 0; i < data.length; i++) total += data[i];
    if (total <= 0) total = 1;
    var cx = ctx.w / 2, cy = ctx.h / 2;
    var r = Math.min(ctx.plotW, ctx.plotH) / 2 - 4;
    var startA = cfg.options.startAngle;
    var g = el('g', { 'class': 'ds-chart__pie' }, svg);
    var items = [];
    for (var j = 0; j < data.length; j++) {
      var sweep = (data[j] / total) * 360;
      var endA = startA + sweep;
      if (endA - startA >= 359.9) endA = startA + 359.9;
      var p = el('path', {
        'class': 'ds-chart__slice',
        d: arcPath(cx, cy, r, 0, startA, endA),
        tabindex: '0',
        'data-index': j,
        'data-value': data[j],
        'data-label': labels[j] || '',
        role: 'img',
        'aria-label': (labels[j] || '') ? (labels[j] + ': ' + data[j]) : String(data[j])
      }, g);
      p.style.setProperty('--color', colors[j % colors.length]);
      items.push(p);
      startA = endA;
    }
    return { items: items, meta: { cx: cx, cy: cy } };
  }

  /* ---------- Renderer: Donut ---------- */
  function renderDonut(svg, cfg, ctx) {
    // P1-5: 环形图必须保持比例，避免拉伸为椭圆（与 multi-donut 一致）
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    // ---- Multi-donut mode ----
    if (cfg.series && cfg.series.length > 1) {
      return renderMultiDonut(svg, cfg, ctx);
    }
    // ---- Single donut logic ----
    var o = cfg.options;
    var cx = ctx.w / 2, cy = ctx.h / 2;
    var r = Math.min(ctx.plotW, ctx.plotH) / 2 - 4;
    var rInner = r * o.donutHole;

    // Single-value donut (like a gauge/progress)
    if (cfg.value != null) {
      var pct = Math.min(Math.max(cfg.value, 0), 100);
      var ring = el('circle', {
        'class': 'ds-chart__donut-ring',
        cx: cx, cy: cy, r: ((r + rInner) / 2).toFixed(2),
        'pathLength': '100'
      }, svg);
      var seg = el('circle', {
        'class': 'ds-chart__donut-seg',
        cx: cx, cy: cy, r: ((r + rInner) / 2).toFixed(2),
        'pathLength': '100',
        'stroke-dasharray': pct + ' ' + (100 - pct),
        'stroke-dashoffset': '0',
        transform: 'rotate(' + o.startAngle + ' ' + cx + ' ' + cy + ')'
      }, svg);
      seg.style.setProperty('--color', cfg._singleColor);
      // P1-4: 透明整圆 hit 作为唯一可聚焦元素，seg 仅为视觉展示，去除 tabindex 避免双重 Tab
      var hit = el('circle', {
        'class': 'ds-chart__donut-hit',
        cx: cx, cy: cy, r: r.toFixed(2),
        fill: 'transparent',
        tabindex: '0',
        'data-value': cfg.value,
        'data-label': (cfg.labels && cfg.labels[0]) || '',
        role: 'img',
        'aria-label': cfg.value + '%'
      }, svg);
      hit.style.setProperty('--color', cfg._singleColor);
      var txt = el('g', { 'class': 'ds-chart__donut-text' }, svg);
      var captionLabel = (cfg.labels && cfg.labels[0]) || '';
      if (captionLabel) {
        var tc = el('text', {
          'class': 'ds-chart__donut-caption',
          x: cx, y: cy - 12, 'text-anchor': 'middle',
          'dominant-baseline': 'central'
        }, txt);
        tc.textContent = captionLabel;
      }
      var tv = el('text', {
        'class': 'ds-chart__donut-value',
        x: cx, y: cy + 8, 'text-anchor': 'middle',
        'dominant-baseline': 'central'
      }, txt);
      tv.textContent = pct + '%';
      return { items: [hit], meta: { cx: cx, cy: cy } };
    }

    // Multi-slice donut (like pie with hole)
    var data = cfg.data || [];
    var labels = cfg.labels || [];
    var colors = o.colors.length ? o.colors : COLOR_DEFAULTS;
    var total = 0;
    for (var i = 0; i < data.length; i++) total += data[i];
    if (total <= 0) total = 1;
    var startA = o.startAngle;
    var g = el('g', { 'class': 'ds-chart__donut' }, svg);
    var items = [];
    for (var j = 0; j < data.length; j++) {
      var sweep = (data[j] / total) * 360;
      var endA = startA + sweep;
      if (endA - startA >= 359.9) endA = startA + 359.9;
      var p = el('path', {
        'class': 'ds-chart__slice',
        d: arcPath(cx, cy, r, rInner, startA, endA),
        tabindex: '0',
        'data-index': j,
        'data-value': data[j],
        'data-label': labels[j] || '',
        role: 'img',
        'aria-label': (labels[j] || '') ? (labels[j] + ': ' + data[j]) : String(data[j])
      }, g);
      p.style.setProperty('--color', colors[j % colors.length]);
      items.push(p);
      startA = endA;
    }
    return { items: items, meta: { cx: cx, cy: cy } };
  }

  /* ---------- Renderer: Multi-Donut ---------- */
  function renderMultiDonut(svg, cfg, ctx) {
    var o = cfg.options;
    var n = cfg.series.length;
    var perW = 200, perH = 200;
    var totalW = perW * n, totalH = perH;
    svg.setAttribute('viewBox', '0 0 ' + totalW + ' ' + totalH);
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    svg.classList.add('ds-chart__svg--donut-multi');
    // 每环渲染 160px（匹配标准环形图），总宽 = n × 160px
    svg.style.width = (n * 160) + 'px';
    var items = [];
    var donutSize = 160;
    var r = donutSize / 2 - 10;
    var rInner = r * o.donutHole;
    for (var i = 0; i < n; i++) {
      var s = cfg.series[i];
      var cx = perW * i + perW / 2;
      var cy = perH / 2 - 10;
      var g = el('g', { 'class': 'ds-chart__donut ds-chart__donut--multi', 'data-series-index': i }, svg);
      if (s.value != null) {
        // Single-value ring
        var pct = Math.min(Math.max(s.value, 0), 100);
        var ringR = (r + rInner) / 2;
        el('circle', { 'class': 'ds-chart__donut-ring', cx: cx, cy: cy, r: ringR.toFixed(2), pathLength: '100' }, g);
        var seg = el('circle', {
          'class': 'ds-chart__donut-seg', cx: cx, cy: cy, r: ringR.toFixed(2), pathLength: '100',
          'stroke-dasharray': pct + ' ' + (100 - pct),
          transform: 'rotate(' + o.startAngle + ' ' + cx + ' ' + cy + ')',
          tabindex: '0', 'data-value': s.value, 'data-label': s.name || '',
          role: 'img', 'aria-label': (s.name || '') + ' ' + s.value + '%'
        }, g);
        seg.style.setProperty('--color', s.color || o.colors[i] || COLOR_DEFAULTS[i % COLOR_DEFAULTS.length]);
        items.push(seg);
        var txt = el('g', { 'class': 'ds-chart__donut-text' }, g);
        var tv = el('text', { 'class': 'ds-chart__donut-value', x: cx, y: cy + 6, 'text-anchor': 'middle', 'dominant-baseline': 'central' }, txt);
        tv.textContent = pct + '%';
      } else if (s.data && s.data.length) {
        // Multi-slice ring
        var data = s.data, labels = s.labels || [];
        var colors = (s.colors && s.colors.length) ? s.colors : (o.colors.length ? o.colors : COLOR_DEFAULTS);
        var total = 0;
        for (var d = 0; d < data.length; d++) total += data[d];
        if (total <= 0) total = 1;
        var startA = o.startAngle;
        for (var j = 0; j < data.length; j++) {
          var sweep = (data[j] / total) * 360;
          var endA = startA + sweep;
          if (endA - startA >= 359.9) endA = startA + 359.9;
          var p = el('path', {
            'class': 'ds-chart__slice', d: arcPath(cx, cy, r, rInner, startA, endA),
            tabindex: '0', 'data-index': j, 'data-value': data[j], 'data-label': labels[j] || '',
            'data-series-index': i, role: 'img'
          }, g);
          p.style.setProperty('--color', colors[j % colors.length]);
          items.push(p);
          startA = endA;
        }
      }
      // Group label at bottom
      if (s.name) {
        var gl = el('text', { 'class': 'ds-chart__donut-group-label', x: cx, y: perH - 16, 'text-anchor': 'middle', fill: 'currentColor' }, g);
        gl.textContent = s.name;
      }
    }
    return { items: items, meta: { multi: true } };
  }

  /* ---------- Renderer: Sparkline ---------- */
  function renderSparkline(svg, cfg, ctx) {
    var data = cfg.data || [];
    // P1-4: 空数据守卫
    if (!data.length) return { items: [], hitRects: [], meta: {} };
    var color = cfg._singleColor;
    var o = cfg.options;
    var min = Infinity, max = -Infinity;
    for (var i = 0; i < data.length; i++) {
      if (data[i] < min) min = data[i];
      if (data[i] > max) max = data[i];
    }
    if (max === min) { max = min + 1; }
    var yScale = scaleLinear(min, max, ctx.h, 0);
    var stepX = ctx.w / (data.length - 1 || 1);
    var pts = [];
    for (var j = 0; j < data.length; j++) {
      var x = j * stepX;
      var y = yScale(data[j]);
      pts.push(x.toFixed(1) + ',' + y.toFixed(1));
    }

    // 1. Baseline
    if (o.baseline !== false) {
      el('line', { 'class': 'ds-chart__sparkline-baseline', x1: 0, y1: (ctx.h - 0.5).toFixed(1), x2: ctx.w, y2: (ctx.h - 0.5).toFixed(1) }, svg);
    }

    // 2. Area fill (default on)
    // Sparkline area fill defaults ON, independent of line/area `fill` option
    if (o.area !== false && data.length >= 2) {
      var areaPts = pts.slice();
      areaPts.push(ctx.w.toFixed(1) + ',' + ctx.h);
      areaPts.unshift('0,' + ctx.h);
      var area = el('path', { 'class': 'ds-chart__area ds-chart__sparkline-area', d: 'M' + areaPts.join(' L') + ' Z' }, svg);
      area.style.setProperty('--color', color);
    }

    // 3. Main line
    var path = el('path', { 'class': 'ds-chart__line', d: 'M' + pts.join(' L') }, svg);
    path.style.setProperty('--color', color);

    // 4. Endpoint dot
    if (o.endpoint !== false && data.length >= 1) {
      var lastX = (data.length - 1) * stepX;
      var lastY = yScale(data[data.length - 1]);
      el('circle', {
        'class': 'ds-chart__sparkline-endpoint',
        cx: lastX.toFixed(1), cy: lastY.toFixed(1), r: 2.5,
        fill: color
      }, svg);
    }
    return { items: [path], meta: { yScale: yScale, stepX: stepX } };
  }

  /* ---------- Renderer: Line ---------- */
  function renderLine(svg, cfg, ctx) {
    var data = cfg.data || [];
    // P1-4: 空数据守卫
    if (!data.length) return { items: [], hitRects: [], meta: {} };
    var labels = cfg.labels || [];
    var color = cfg._singleColor;
    var o = cfg.options;
    var min = Infinity, max = -Infinity;
    for (var i = 0; i < data.length; i++) {
      if (data[i] < min) min = data[i];
      if (data[i] > max) max = data[i];
    }
    if (max === min) { max = min + 1; }
    if (o.yAxis && o.yAxis.min && o.yAxis.min !== 'auto') min = o.yAxis.min;
    else if (o.yMin && o.yMin !== 'auto') min = o.yMin;
    if (o.yAxis && o.yAxis.max && o.yAxis.max !== 'auto') max = o.yAxis.max;
    else if (o.yMax && o.yMax !== 'auto') max = o.yMax;
    var yScale = scaleLinear(min, max, ctx.h - ctx.padB, ctx.padT);
    yScale._min = min; yScale._max = max;
    var xBand = scaleBand(data.length, ctx.padL, ctx.w - ctx.padR, 0);
    var stepX = ctx.plotW / data.length;
    var bw = stepX;

    drawAxes(svg, ctx, cfg, { x: xBand, y: yScale, xType: 'band', yType: 'linear' });

    var pts = [];
    var dots = [];
    for (var j = 0; j < data.length; j++) {
      var x = ctx.padL + (j + 0.5) * stepX; // center-aligned with category tick
      var y = yScale(data[j]);
      pts.push(x.toFixed(1) + ',' + y.toFixed(1));
      dots.push({ x: x, y: y, v: data[j] });
    }

    var g = el('g', { 'class': 'ds-chart__line' }, svg);

    if (o.fill) {
      var firstX = dots[0].x, lastX = dots[dots.length - 1].x;
      var area = el('path', {
        'class': 'ds-chart__area',
        d: 'M' + pts.join(' L') + ' L' + lastX.toFixed(1) + ',' + (ctx.h - ctx.padB) +
           ' L' + firstX.toFixed(1) + ',' + (ctx.h - ctx.padB) + ' Z'
      }, g);
      area.style.setProperty('--color', color);
    }

    var path = el('path', {
      'class': 'ds-chart__line',
      d: 'M' + pts.join(' L')
    }, g);
    path.style.setProperty('--color', color);

    var dotEls = [];
    if (o.dots) {
      for (var d = 0; d < dots.length; d++) {
        var dc = el('circle', {
          'class': 'ds-chart__dot',
          cx: dots[d].x.toFixed(1),
          cy: dots[d].y.toFixed(1),
          r: '2',
          'data-index': d,
          'data-value': data[d],
          'data-label': labels[d] || ''
        }, g);
        dc.style.setProperty('--color', color);
        dotEls.push(dc);
      }
    }

    // transparent hit zones — centered on each data point
    var hitG = el('g', { 'class': 'ds-chart__hit-zones' }, svg);
    var hitRects = [];
    var colW = ctx.plotW / data.length;
    for (var h = 0; h < data.length; h++) {
      var hx = ctx.padL + (h + 0.5) * colW - colW / 2;
      var hw = colW;
      if (data.length === 1) hw = ctx.plotW;
      var hr = el('rect', {
        'class': 'ds-chart__hit-zone',
        x: hx.toFixed(1),
        y: ctx.padT,
        width: hw.toFixed(1),
        height: ctx.plotH.toFixed(1),
        fill: 'transparent',
        tabindex: '0',
        'data-index': h,
        role: 'img',
        'aria-label': (labels[h] || '') ? (labels[h] + ': ' + data[h]) : String(data[h])
      }, hitG);
      hitRects.push(hr);
    }

    return {
      items: [path],
      dots: dotEls,
      hitRects: hitRects,
      meta: { yScale: yScale, xBand: xBand, bw: bw, data: data, labels: labels, series: [{ name: cfg.title || 'Value', color: color, data: data }] }
    };
  }

  /* ---------- Renderer: Multi / Combo ---------- */
  function renderMulti(svg, cfg, ctx) {
    var series = cfg.series || [];
    var labels = cfg.labels || [];
    var o = cfg.options;
    // P1-4: 空数据守卫
    if (!series.length) return { items: [], hitRects: [], meta: {} };
    var dataLen = 0;
    for (var si = 0; si < series.length; si++) {
      if (series[si].data && series[si].data.length > dataLen) dataLen = series[si].data.length;
    }
    var allMin = Infinity, allMax = -Infinity;
    for (var sj = 0; sj < series.length; sj++) {
      var d = series[sj].data;
      for (var di = 0; di < d.length; di++) {
        if (d[di] < allMin) allMin = d[di];
        if (d[di] > allMax) allMax = d[di];
      }
    }
    if (allMax === allMin) { allMax = allMin + 1; }
    if (allMin > 0) allMin = 0;
    if (o.yAxis && o.yAxis.min && o.yAxis.min !== 'auto') allMin = o.yAxis.min;
    else if (o.yMin && o.yMin !== 'auto') allMin = o.yMin;
    if (o.yAxis && o.yAxis.max && o.yAxis.max !== 'auto') allMax = o.yAxis.max;
    else if (o.yMax && o.yMax !== 'auto') allMax = o.yMax;
    var yScale = scaleLinear(allMin, allMax, ctx.h - ctx.padB, ctx.padT);
    yScale._min = allMin; yScale._max = allMax;
    var xBand = scaleBand(dataLen, ctx.padL, ctx.w - ctx.padR, 0);

    drawAxes(svg, ctx, cfg, { x: xBand, y: yScale, xType: 'band', yType: 'linear' });

    // count bar series for grouping
    var barSeries = [];
    var lineSeries = [];
    for (var sk = 0; sk < series.length; sk++) {
      if (series[sk].chartType === 'bar') barSeries.push(series[sk]);
      else lineSeries.push(series[sk]);
    }

    var items = [];
    var dotEls = [];
    var gBars = null, gLines = null;

    // Bars (grouped)
    if (barSeries.length) {
      gBars = el('g', { 'class': 'ds-chart__bars ds-chart__bars--grouped' }, svg);
      var colW = ctx.plotW / dataLen;
      var groupW = clampBarWidth(colW);
      var groupPad = colW - groupW;
      var barW = groupW / barSeries.length;
      for (var bi = 0; bi < barSeries.length; bi++) {
        var bs = barSeries[bi];
        for (var bj = 0; bj < bs.data.length; bj++) {
          var v = bs.data[bj];
          var by = yScale(Math.max(v, 0));
          var bh = (ctx.h - ctx.padB) - by;
          if (bh < 0) bh = 0;
          var bx = ctx.padL + bj * colW + groupPad / 2 + bi * barW;
          var rect = el('rect', {
            'class': 'ds-chart__bar',
            x: bx.toFixed(1),
            y: by.toFixed(1),
            width: barW.toFixed(1),
            height: bh.toFixed(1),
            tabindex: '0',
            'data-index': bj,
            'data-series': bi,
            'data-value': v,
            'data-label': labels[bj] || '',
            'data-series-name': bs.name || '',
            role: 'img',
            'aria-label': (labels[bj] || '') ? (labels[bj] + ': ' + v) : String(v)
          }, gBars);
          rect.style.setProperty('--color', bs.color);
          if (cfg.options.animate) rect.style.setProperty('--d', (bj * 40) + 'ms');
          items.push(rect);
        }
      }
    }

    // Lines
    if (lineSeries.length) {
      gLines = el('g', { 'class': 'ds-chart__lines ds-chart__line' }, svg);
      var stepX = ctx.plotW / dataLen;
      for (var li = 0; li < lineSeries.length; li++) {
        var ls = lineSeries[li];
        var pts = [];
        for (var lp = 0; lp < ls.data.length; lp++) {
          var px = ctx.padL + (lp + 0.5) * stepX; // center-aligned with category tick
          var py = yScale(ls.data[lp]);
          pts.push(px.toFixed(1) + ',' + py.toFixed(1));
        }
        var lpEl = el('path', {
          'class': 'ds-chart__line',
          d: 'M' + pts.join(' L')
        }, gLines);
        lpEl.style.setProperty('--color', ls.color);
        lpEl.setAttribute('data-series', li);
        items.push(lpEl);
        if (o.dots) {
          for (var ld = 0; ld < ls.data.length; ld++) {
            var dc = el('circle', {
              'class': 'ds-chart__dot',
              cx: (ctx.padL + (ld + 0.5) * stepX).toFixed(1),
              cy: yScale(ls.data[ld]).toFixed(1),
              r: '2',
              'data-index': ld,
              'data-series': li,
              'data-value': ls.data[ld]
            }, gLines);
            dc.style.setProperty('--color', ls.color);
            dotEls.push(dc);
          }
        }
      }
    }

    // P1-5: 仅当存在折线系列时创建共享 hit zone（纯柱场景柱条自身已有 tabindex，避免双重 Tab）
    var hitG = null, hitRects = [];
    if (lineSeries.length > 0) {
      hitG = el('g', { 'class': 'ds-chart__hit-zones' }, svg);
      var colWidth = ctx.plotW / dataLen;
      for (var h = 0; h < dataLen; h++) {
        var hx = ctx.padL + (h + 0.5) * colWidth - colWidth / 2;
        var hw = colWidth;
        if (dataLen === 1) hw = ctx.plotW;
        // 构建 aria-label：拼接该列所有系列的值
        var hitLabelParts = [];
        for (var hs = 0; hs < series.length; hs++) {
          var sv = series[hs].data[h];
          if (sv != null) {
            hitLabelParts.push((series[hs].name || ('Series ' + (hs + 1))) + ': ' + sv);
          }
        }
        var hr = el('rect', {
          'class': 'ds-chart__hit-zone',
          x: hx.toFixed(1),
          y: ctx.padT,
          width: hw.toFixed(1),
          height: ctx.plotH.toFixed(1),
          fill: 'transparent',
          tabindex: '0',
          'data-index': h,
          role: 'img',
          'aria-label': (labels[h] || ('Item ' + (h + 1))) + ' — ' + hitLabelParts.join(', ')
        }, hitG);
        hitRects.push(hr);
      }
    }

    return {
      items: items,
      dots: dotEls,
      hitRects: hitRects,
      meta: { yScale: yScale, xBand: xBand, series: series, labels: labels }
    };
  }

  /* ---------- Legend ---------- */
  function drawLegend(host, cfg, meta) {
    var series = (cfg.series && cfg.series.length) ? cfg.series : null;
    if (!series) {
      if (cfg.type === 'pie' || cfg.type === 'donut') {
        if (!cfg.labels || !cfg.data) return;
        series = [];
        var colors = cfg.options.colors.length ? cfg.options.colors : COLOR_DEFAULTS;
        for (var i = 0; i < cfg.data.length; i++) {
          series.push({ name: cfg.labels[i] || String(i + 1), color: colors[i % colors.length] });
        }
      } else {
        return;
      }
    }
    var leg = document.createElement('div');
    leg.className = 'ds-chart__legend';
    var itemsArr = [];
    for (var j = 0; j < series.length; j++) {
      var item = document.createElement('span');
      item.className = 'ds-chart__legend-item';
      item.setAttribute('data-series', j);
      item.setAttribute('tabindex', '0');
      var sw = document.createElement('span');
      sw.className = 'ds-chart__legend-swatch';
      sw.style.background = series[j].color;
      item.appendChild(sw);
      item.appendChild(document.createTextNode(series[j].name || ('Series ' + (j + 1))));
      leg.appendChild(item);
      itemsArr.push(item);
    }
    host.appendChild(leg);

    // Hover/focus → highlight series; dim others
    var allItems = meta.items || [];
    function setHighlight(idx) {
      for (var k = 0; k < allItems.length; k++) {
        var it = allItems[k];
        // P1-3: pie/donut 切片用 data-index 表示系列索引，fallback 兼容
        var si = it.getAttribute('data-series');
        if (si == null) si = it.getAttribute('data-index');
        if (si == null) continue;
        var on = String(si) === String(idx);
        it.style.opacity = on ? '1' : '0.25';
      }
    }
    function clearHighlight() {
      for (var k = 0; k < allItems.length; k++) {
        allItems[k].style.opacity = '';
      }
    }
    for (var m = 0; m < itemsArr.length; m++) {
      (function (mi) {
        itemsArr[mi].addEventListener('mouseenter', function () { setHighlight(mi); });
        itemsArr[mi].addEventListener('mouseleave', clearHighlight);
        itemsArr[mi].addEventListener('focus', function () { setHighlight(mi); });
        itemsArr[mi].addEventListener('blur', clearHighlight);
      })(m);
    }
  }

  /* ---------- Tooltip (singleton) ---------- */
  var tooltipEl = null;
  function ensureTooltip() {
    if (tooltipEl) return tooltipEl;
    tooltipEl = document.createElement('div');
    tooltipEl.className = 'ds-chart__tooltip';
    tooltipEl.setAttribute('role', 'tooltip');
    tooltipEl.style.position = 'fixed';
    tooltipEl.style.pointerEvents = 'none';
    tooltipEl.style.opacity = '0';
    tooltipEl.style.transition = 'opacity 150ms ease';
    tooltipEl.style.zIndex = '500';
    document.body.appendChild(tooltipEl);
    return tooltipEl;
  }

  function showTooltip(evt, items) {
    var tip = ensureTooltip();
    // P2-1: 使用 DOM API 构建，避免 innerHTML XSS
    // 先清空旧内容
    while (tip.firstChild) tip.removeChild(tip.firstChild);
    if (items.label) {
      var titleEl = document.createElement('div');
      titleEl.className = 'ds-chart__tooltip-title';
      titleEl.textContent = items.label;
      tip.appendChild(titleEl);
    }
    if (items.values && items.values.length) {
      for (var i = 0; i < items.values.length; i++) {
        var v = items.values[i];
        var row = document.createElement('div');
        row.className = 'ds-chart__tooltip-row';
        var swatch = document.createElement('span');
        swatch.className = 'ds-chart__tooltip-swatch';
        swatch.style.background = v.color;
        row.appendChild(swatch);
        if (v.name) {
          var nameEl = document.createElement('span');
          nameEl.className = 'ds-chart__tooltip-name';
          nameEl.textContent = v.name;
          row.appendChild(nameEl);
        }
        var valEl = document.createElement('span');
        valEl.className = 'ds-chart__tooltip-value';
        valEl.textContent = v.value;
        row.appendChild(valEl);
        tip.appendChild(row);
      }
    }
    tip.style.opacity = '1';
    // position
    var x = evt.clientX + 12;
    var y = evt.clientY + 12;
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    if (x + tw > window.innerWidth - 8) x = evt.clientX - tw - 12;
    if (y + th > window.innerHeight - 8) y = evt.clientY - th - 12;
    tip.style.left = x + 'px';
    tip.style.top = y + 'px';
  }

  function hideTooltip() {
    if (tooltipEl) tooltipEl.style.opacity = '0';
  }

  /* ---------- Interactions ---------- */
  function bindInteractions(svg, cfg, ctx, result) {
    var type = cfg.type;
    var o = cfg.options;
    if (!o.tooltip) return;
    var items = result.items;
    var hitRects = result.hitRects;
    var meta = result.meta;

    function labelFor(idx) {
      if (cfg.labels && cfg.labels[idx]) return cfg.labels[idx];
      return String(idx + 1);
    }

    // Line / multi / combo: use hit zones
    if (hitRects && hitRects.length) {
      var seriesArr = meta.series || [];
      for (var i = 0; i < hitRects.length; i++) {
        (function (idx) {
          var hr = hitRects[idx];
          function onEnter(e) {
            var values = [];
            for (var s = 0; s < seriesArr.length; s++) {
              var sd = seriesArr[s].data;
              if (sd && idx < sd.length) {
                values.push({ name: seriesArr[s].name || '', value: sd[idx], color: seriesArr[s].color });
              }
            }
            showTooltip(e, { label: labelFor(idx), values: values });
            // highlight dot
            if (result.dots) {
              for (var d = 0; d < result.dots.length; d++) {
                if (String(result.dots[d].getAttribute('data-index')) === String(idx)) {
                  result.dots[d].classList.add('is-hover');
                }
              }
            }
          }
          function onLeave() {
            hideTooltip();
            if (result.dots) {
              for (var d = 0; d < result.dots.length; d++) {
                result.dots[d].classList.remove('is-hover');
              }
            }
          }
          hr.addEventListener('mousemove', function (e) {
            onEnter(e);
          });
          hr.addEventListener('mouseleave', onLeave);
          hr.addEventListener('focus', function (e) {
            onEnter({ clientX: hr.getBoundingClientRect().left + hr.getBoundingClientRect().width / 2, clientY: hr.getBoundingClientRect().top });
          });
          hr.addEventListener('blur', onLeave);
        })(i);
      }
      return;
    }

    // Bar / pie / donut / hbar / stacked: per-item
    for (var j = 0; j < items.length; j++) {
      (function (it) {
        function onEnter(e) {
          var v = it.getAttribute('data-value');
          var lbl = it.getAttribute('data-label') || '';
          var sn = it.getAttribute('data-series-name');
          var color = getComputedStyle(it).getPropertyValue('--color').trim() || 'var(--ds-chart-1)';
          var values = [{ name: sn || '', value: v, color: color }];
          showTooltip(e, { label: lbl, values: values });
          it.classList.add('is-hover');
        }
        function onLeave() {
          hideTooltip();
          it.classList.remove('is-hover');
        }
        it.addEventListener('mouseenter', onEnter);
        it.addEventListener('mouseleave', onLeave);
        it.addEventListener('focus', function (e) {
          var r = it.getBoundingClientRect();
          onEnter({ clientX: r.left + r.width / 2, clientY: r.top + r.height / 2 });
        });
        it.addEventListener('blur', onLeave);
      })(items[j]);
    }
  }

  /* ---------- Animations ---------- */
  function animEnter(svg, type, cfg) {
    if (!cfg.options.animate) return;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) return;

    // Bar types: CSS class-driven scaleY (add class to svg for descendant selector)
    if (type === 'bar' || type === 'hbar' || type === 'stacked') {
      svg.classList.add('ds-chart--anim-in');
      return;
    }

    // Line types: stroke-dashoffset draw-in
    if (type === 'line' || type === 'multiline' || type === 'combo' || type === 'sparkline') {
      var paths = svg.querySelectorAll('path.ds-chart__line');
      for (var p = 0; p < paths.length; p++) {
        var path = paths[p];
        try {
          var len = path.getTotalLength();
          path.style.strokeDasharray = len;
          path.style.strokeDashoffset = len;
          // force reflow then transition
          // eslint-disable-next-line no-unused-expressions
          path.getBoundingClientRect();
          path.style.transition = 'stroke-dashoffset 700ms cubic-bezier(0.16, 1, 0.3, 1)';
          path.style.strokeDashoffset = '0';
        } catch (e) { console.warn('[EDIC chart] getTotalLength failed', e); }
      }
      return;
    }

    // Pie/donut: CSS-driven staggered fade-in + group-scale zoom (class-based)
    if (type === 'pie' || type === 'donut') {
      svg.classList.add('ds-chart--anim-in');
      var slices = svg.querySelectorAll('.ds-chart__slice, .ds-chart__donut-seg');
      for (var s = 0; s < slices.length; s++) {
        slices[s].style.setProperty('--d', (s * 80) + 'ms');
      }
      // 动画结束后移除 ds-chart--anim-in，避免 animation-fill-mode:both
      // 的 forwards 语义持续覆盖内联 opacity，导致图例高亮失效
      var sliceCount = slices.length;
      if (sliceCount === 0) {
        svg.classList.remove('ds-chart--anim-in');
      } else {
        var finished = 0;
        var onAnimEnd = function(e) {
          if (e.animationName !== 'ds-fade-in') return;
          e.target.removeEventListener('animationend', onAnimEnd);
          finished++;
          if (finished >= sliceCount) {
            svg.classList.remove('ds-chart--anim-in');
          }
        };
        for (var s2 = 0; s2 < slices.length; s2++) {
          slices[s2].addEventListener('animationend', onAnimEnd);
        }
      }
    }
  }

  /* ---------- Data table (sr-only fallback) ---------- */
  function buildDataTable(cfg) {
    var tbl = document.createElement('table');
    tbl.className = 'ds-sr-only';
    // sr-only 类已保证视觉隐藏但读屏可读，无需额外 aria-hidden
    if (cfg.title) {
      var cap = document.createElement('caption');
      cap.textContent = cfg.title;
      tbl.appendChild(cap);
    }

    // P1-6: 单值环形图（gauge）数据在 cfg.value，特殊处理
    if (cfg.value != null && !cfg.data && !(cfg.series && cfg.series.length)) {
      var thead0 = document.createElement('thead');
      var trh0 = document.createElement('tr');
      var th0 = document.createElement('th');
      th0.textContent = 'Label';
      trh0.appendChild(th0);
      var thv0 = document.createElement('th');
      thv0.textContent = 'Value';
      trh0.appendChild(thv0);
      thead0.appendChild(trh0);
      tbl.appendChild(thead0);
      var tbody0 = document.createElement('tbody');
      var tr0 = document.createElement('tr');
      var tdLabel = document.createElement('td');
      tdLabel.textContent = (cfg.labels && cfg.labels[0]) || cfg.title || 'Value';
      tr0.appendChild(tdLabel);
      var tdVal = document.createElement('td');
      tdVal.textContent = cfg.value + '%';
      tr0.appendChild(tdVal);
      tbody0.appendChild(tr0);
      tbl.appendChild(tbody0);
      return tbl;
    }
    var thead = document.createElement('thead');
    var trh = document.createElement('tr');
    var th0 = document.createElement('th');
    th0.textContent = 'Label';
    trh.appendChild(th0);
    if (cfg.series && cfg.series.length) {
      for (var s = 0; s < cfg.series.length; s++) {
        var th = document.createElement('th');
        th.textContent = cfg.series[s].name || ('Series ' + (s + 1));
        trh.appendChild(th);
      }
    } else {
      var thv = document.createElement('th');
      thv.textContent = 'Value';
      trh.appendChild(thv);
    }
    thead.appendChild(trh);
    tbl.appendChild(thead);

    var tbody = document.createElement('tbody');
    var labels = cfg.labels || [];
    var rows = Math.max(labels.length, (cfg.data && cfg.data.length) || 0);
    if (cfg.series && cfg.series.length) {
      rows = cfg.series[0].data ? cfg.series[0].data.length : 0;
    }
    for (var i = 0; i < rows; i++) {
      var tr = document.createElement('tr');
      var td0 = document.createElement('td');
      td0.textContent = labels[i] || String(i + 1);
      tr.appendChild(td0);
      if (cfg.series && cfg.series.length) {
        for (var s2 = 0; s2 < cfg.series.length; s2++) {
          var td = document.createElement('td');
          td.textContent = cfg.series[s2].data[i] != null ? cfg.series[s2].data[i] : '';
          tr.appendChild(td);
        }
      } else {
        var td1 = document.createElement('td');
        td1.textContent = cfg.data && cfg.data[i] != null ? cfg.data[i] : '';
        tr.appendChild(td1);
      }
      tbody.appendChild(tr);
    }
    tbl.appendChild(tbody);
    return tbl;
  }

  /* ---------- Unified entry ---------- */
  function renderChart(host, rawCfg) {
    var cfg = normalizeConfig(rawCfg);
    var type = cfg.type;

    // SR-only data table
    host.appendChild(buildDataTable(cfg));

    var ctx = makeCtx(cfg);
    var svg = el('svg', {
      'class': 'ds-chart__svg ds-chart__svg--' + type,
      viewBox: '0 0 ' + ctx.w + ' ' + ctx.h,
      preserveAspectRatio: 'none',
      role: 'presentation'
    });

    var result = { items: [], meta: {} };
    switch (type) {
      case 'bar':       result = renderBar(svg, cfg, ctx); break;
      case 'hbar':      result = renderHBar(svg, cfg, ctx); break;
      case 'stacked':   result = renderStacked(svg, cfg, ctx); break;
      case 'pie':       result = renderPie(svg, cfg, ctx); break;
      case 'donut':     result = renderDonut(svg, cfg, ctx); break;
      case 'sparkline': result = renderSparkline(svg, cfg, ctx); break;
      case 'line':      result = renderLine(svg, cfg, ctx); break;
      case 'multiline':
      case 'combo':     result = renderMulti(svg, cfg, ctx); break;
      default: return;
    }

    host.insertBefore(svg, host.firstChild);

    // Visible chart title (before SVG)
    var chartTitle = cfg.title || cfg.options.title || cfg.options.chartTitle;
    if (chartTitle) {
      var titleEl = document.createElement('div');
      titleEl.className = 'ds-chart__title';
      titleEl.textContent = chartTitle;
      host.insertBefore(titleEl, svg);
    }

    // Legend
    if (cfg.options.legend) drawLegend(host, cfg, result);

    // Interactions + tooltip
    if (cfg.options.tooltip) bindInteractions(svg, cfg, ctx, result);

    // Animate
    animEnter(svg, type, cfg);
  }

  /* ---------- Bootstrap ---------- */
  for (var c = 0; c < charts.length; c++) {
    var host = charts[c];
    var raw;
    try { raw = JSON.parse(host.getAttribute('data-chart')); }
    catch (err) { console.warn('[EDIC chart] parse error', err); continue; }
    if (!raw || !raw.type) continue;
    renderChart(host, raw);
  }
})();
