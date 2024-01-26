export default function handleResponseFromAPI(promise) {
  return promise
    .then((res) => {
      console.log(res);
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((err) => err)
    .finally(() => {
      console.log('Got a response from the API');
    });
}
