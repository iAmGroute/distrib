
export function printHash(h) {
  return h.slice(0, 16);
}

export function printDate(unixTime) {
  const d = new Date(unixTime * 1000);
  return d.toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "medium",
    hour12: false
  });
}

export function printDateLong(unixTime) {
  const d = new Date(unixTime * 1000);
  return d.toLocaleString(undefined, {
    dateStyle: "long",
    timeStyle: "long",
    hour12: false
  });
}
