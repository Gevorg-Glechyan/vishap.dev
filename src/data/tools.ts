// One entry per tool. The hub, the footer and the simple product pages read from here.
export const tools = [
  {
    slug: 'screenshot-capture-studio',
    name: 'Screenshot Capture Studio',
    line: 'Captures the visible area, a selected area or the full page of a tab.',
  },
  {
    slug: 'posthog-debugger',
    name: 'PostHog Debugger (Unofficial)',
    line: 'Shows PostHog events in DevTools as a page sends them.',
  },
  {
    slug: 'window-resize-manager',
    name: 'Window Resize Manager',
    line: 'Sets any Chrome window to an exact size.',
  },
] as const;
