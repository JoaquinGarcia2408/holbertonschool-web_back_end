export default function cleanSet(set, startString) {
  if (startString === '' || !startString) {
    return '';
  }
  if (typeof startString !== 'string') {
    return '';
  }
  const arrayFromSet = Array.from(set);
  const filteredValues = arrayFromSet
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return filteredValues.join('-');
}
