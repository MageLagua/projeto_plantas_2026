import { defineComponent, ref } from 'vue'
import loadingImg from './../../assets/loading.jpeg'

export default defineComponent({
  name: 'Page',
  setup() {
    const imageUrl = ref<string>('')
    const plantName = ref<string>('')
    const goodFor = ref<string>('')
    let file: File | undefined

    function onFileChange(event: Event) {
      file = (event.target as HTMLInputElement).files?.[0]
      if (file) imageUrl.value = URL.createObjectURL(file)
    }

    function setGoodFor(data: any) {
        if (data.poisonToCats === "safe" && data.poisonToDogs === "safe"){
            goodFor.value = "Gatos e Cachorros!"
        } else if (data.poisonToDogs === "safe") {
            goodFor.value = "Cachorros apenas!"
        } else if (data.poisonToCats === "safe") {
            goodFor.value = "Gatos apenas!"
        } else {
            goodFor.value = "Venenosa!"
        }
    }

    async function onSubmit() {
      if (!file) return
      const previousUrl = imageUrl.value
      imageUrl.value = loadingImg
      const formData = new FormData()
      formData.append('file', file)
      const response = await fetch('/api/identify', {
        method: 'POST',
        body: formData,
      })
      const data = await response.json()
      console.log(data)
      plantName.value = data.name
      setGoodFor(data)
      imageUrl.value = previousUrl
    }

    return { imageUrl, onFileChange, onSubmit, plantName, goodFor }
  },
})
