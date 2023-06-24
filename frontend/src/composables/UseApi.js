import { api } from 'src/boot/axios'

export default function useApi () {
  const post = async (form) => {
    const url = 'api/v1/loans/'
    const data = { ...form }
    console.log(data)
    await api.post(url, data)
      .then((response) => {
        console.log(response)
        return response
      })
      .catch((error) => {
        console.log(error)
        throw error
      })
  }

  return {
    post
  }
}
