export default function uploadPhoto(fileName) {
  const promise = Promise.reject(new Error(`${fileName} cannot be processed`));
  return promise;
}
