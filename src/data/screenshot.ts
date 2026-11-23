// Screenshot Capture Studio: facts and copy for the product section.
// Source of truth for the wording: the extension's own docs and store listing
// (screenshot-extension/docs, glechyan.com/src/content/screenshot-landing.ts). Do not invent features here.

export const slug = 'screenshot-capture-studio';
export const name = 'Screenshot Capture Studio';
export const accent = 'product-teal';
export const accentText = { light: '#0F6B63', dark: '#6BD0C3' };

const listing = 'https://chromewebstore.google.com/detail/screenshot-capture-studio/pdncfimfmepmkiodikhpbhodhanfilhf';
/** Chrome Web Store link, tagged by where on the page the button sits, so installs can be told apart. */
export const store = (placement: string) => `${listing}?utm_source=vishap.dev&utm_medium=landing&utm_campaign=${placement}`;

/** The page's own address, for visitors on a phone who need to open it on a computer. */
export const pageUrl = 'https://vishap.dev/screenshot-capture-studio/';

// Support and policies still live on the old site until they are moved here (plan steps 3 to 5).
const old = 'https://glechyan.com/extensions/screenshot';
export const links = {
  support: `${old}/support/`,
  privacy: `${old}/privacy-policy/`,
  docs: `${old}/docs/`,
};

export const price = { monthly: '$4', yearly: '$40', saving: '$8', trial: '3-day free trial. Cancel any time.' };

export const captureModes = [
  { name: 'Full page', text: 'Capture a scrolling page from top to bottom as one image.' },
  { name: 'Visible area', text: 'Capture the visible page content in the current Chrome tab.' },
  { name: 'Selected area', text: 'Draw around the part of the page you want to capture.' },
];

export const tools = 'Arrow, line, pen, highlighter, text, rectangle, ellipse, crop and blur.';

export const features = [
  { name: 'Visible-area, selected-area, and full-page capture', detail: 'Capture page content in the current Chrome tab.', free: true },
  { name: 'Editing and local export', detail: 'Arrows, text, shapes, crop, blur, PNG clipboard, and PNG/JPEG/WebP/PDF downloads.', free: true },
  { name: 'History on this device', detail: 'Reopen, rename, pin, and delete recent captures with saved edits.', free: true },
  { name: 'Configurable capture shortcuts', detail: 'Chrome suggests Alt+Shift+V, A and F, and may leave one unassigned if it clashes. Change them in Chrome’s shortcut settings.', free: true },
  { name: 'HTML element capture', detail: 'Select a same-document element or visible scrollable container. Long elements in scrolling feeds are captured in full.', free: false },
  { name: 'Bulk tab capture', detail: 'Capture from selected tabs, up to 30 per job, with optional site access for web capture.', free: false },
  { name: 'Custom filename patterns', detail: 'Reuse a filename pattern for repeat work.', free: false },
  { name: 'Google Drive and Dropbox upload', detail: 'Where available: connect a provider, choose a folder, then select Upload to send the edited PNG.', free: false },
  { name: 'Linear and GitHub screenshot handoff', detail: 'Connect Linear or GitHub and choose Create issue to upload the edited screenshot, then complete and submit the issue there.', free: false },
];

// The Premium workflows, worded for the landing page. The comparison table below keeps the formal names.
export const premiumCards = [
  { name: 'Capture one element', text: 'Click one element, such as a table, a card or a thread, and capture only that. Long scrolling elements are captured in full.' },
  { name: 'Capture many tabs at once', text: 'Choose the tabs, up to 30 per job, and capture each one. Chrome asks for access to those sites when the job runs.' },
  { name: 'Name files your way', text: 'Set a filename pattern once, built from the site, the capture mode, the date and the time.' },
  { name: 'Upload to Google Drive or Dropbox', text: 'Connect a provider, choose a folder, then choose Upload to send the edited PNG. Offered where the provider is available.' },
  { name: 'Create a Linear or GitHub issue', text: 'Choose Create issue. The edited screenshot uploads, and the issue form opens there for you to finish and submit.' },
];

// How to get Premium. Purchase starts inside the extension, so the page has to say so.
export const premiumSteps = [
  'Add the extension to Chrome and pin it to the toolbar.',
  'Open Settings, then Premium, or choose any action marked with a crown.',
  'Pick monthly or yearly. Checkout opens in a new tab.',
  'Premium turns on in this Chrome installation.',
];

// What Chrome shows at install, in plain words. Source: the extension manifest.
export const permissions = [
  { what: 'The tab you capture', why: 'Only the tab you start a capture on.' },
  { what: 'Scripting', why: 'Runs the selection, element and full-page helpers on that page.' },
  { what: 'Downloads and clipboard', why: 'Saves files to your computer and copies the image.' },
  { what: 'Storage', why: 'Keeps your settings and History on this device.' },
  { what: 'Sign-in and tabs', why: 'Used by Premium: connecting Drive, Dropbox or Linear, and bulk capture.' },
];

export const stays = [
  'Capturing and stitching the page',
  'Editing and annotation',
  'History, with your saved edits',
  'Copying to the clipboard and local downloads',
  'Your settings',
];

export const leaves = [
  { what: 'Usage analytics and error reports', detail: 'A fixed list of events. They never include screenshot pixels, page content, addresses or filenames.' },
  { what: 'Uploads you start', detail: 'The edited PNG goes to Google Drive, Dropbox, Linear or GitHub only when you choose Upload or Create issue.' },
  { what: 'Premium billing', detail: 'Paddle processes the purchase.' },
  { what: 'Uninstall feedback', detail: 'Optional, and only what you choose to write.' },
];

export const steps = [
  'Open the webpage you want to capture and let its content load.',
  'Open Screenshot Capture Studio from Chrome’s toolbar and choose Full page.',
  'Review the result in the editor, make any edits, then copy or download it.',
];

export const faqs = [
  {
    id: 'capture-scope',
    question: 'Does it capture the whole desktop or just a Chrome tab?',
    answer: 'Screenshot Capture Studio captures webpage content in Chrome on desktop. Visible-area capture saves the page content currently in view; full-page capture scrolls and stitches page content locally. Browser toolbars, the tab bar, the address bar, and other applications are outside this scope.',
    link: { label: 'Read capture help', href: links.support },
  },
  {
    id: 'chrome-without-extension',
    question: 'Can Chrome take a full-page screenshot without an extension?',
    answer: 'Yes. Chrome DevTools has a Capture full size screenshot command. Screenshot Capture Studio adds a toolbar workflow with editing, several export formats, and local History. Both approaches can encounter page-layout and browser limits.',
    link: { label: 'Chrome’s screenshot documentation', href: 'https://developer.chrome.com/blog/devtools-tips-33' },
  },
  {
    id: 'download-formats',
    question: 'Which formats can I save? Is the PDF searchable?',
    answer: 'Download PNG, JPEG, WebP, or PDF, or copy the edited PNG to the clipboard. The PDF contains the screenshot image; it does not add OCR or searchable text. Chrome’s Print workflow produces a different kind of document and may change the page layout. WebP supports up to 16,383 pixels per side; use another format or crop larger captures.',
    link: { label: 'Compare download formats', href: `${links.support}#download-formats` },
  },
  {
    id: 'free-and-premium',
    question: 'What is free, and what needs Premium?',
    answer: 'Visible-area, selected-area, and full-page capture, editing, local exports, PNG clipboard, configurable shortcuts, and History are free. Premium adds element capture, bulk tab capture, custom filename patterns, available Google Drive/Dropbox uploads, and Linear and GitHub screenshot handoff.',
    link: { label: 'Compare Free and Premium', href: '#pricing' },
  },
  {
    id: 'local-and-upload',
    question: 'When does a screenshot leave my device?',
    answer: 'Capture, editing, History, clipboard, and local exports are processed on your device. Optional connected workflows send the edited screenshot when you start the provider action. For Google Drive or Dropbox, select a folder and choose Upload. For Linear or GitHub, Create issue uploads the image before opening the composer where you enter and submit the issue details. Usage analytics does not receive screenshot pixels or page content.',
    link: { label: 'Read the privacy policy', href: links.privacy },
  },
  {
    id: 'capture-limits',
    question: 'Why might a full-page screenshot miss content or fail?',
    answer: 'Chrome stops extensions from capturing some of its own pages and other protected pages. Lazy-loaded content, scroll-triggered animations, competing scroll areas, and very large pages can also produce incomplete or repeated content. Let the page finish loading, close moving overlays, and retry. During ordinary full-page scrolling, Escape opens the portion captured so far after the current tile finishes.',
    link: { label: 'Capture help and troubleshooting', href: links.support },
  },
  {
    id: 'history-limits',
    question: 'How much does History keep?',
    answer: 'History keeps up to 100 items or 250 MB on this device, removing the oldest unpinned items first. Pinned items are not removed automatically; if they prevent space being reclaimed, the new History save is skipped. Turning automatic History off preserves existing items. History has no cloud backup or account sync.',
    link: { label: 'Read local storage details', href: `${links.privacy}#local-processing-and-storage` },
  },
];
