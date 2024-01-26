export default function getResponseFromAPI() {
  const aPromise = new Promise((resolve) => {
    setTimeout(resolve, 1000);
  });
  return aPromise;
}
