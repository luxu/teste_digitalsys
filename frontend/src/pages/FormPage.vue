<template>
    <q-page padding="">
      <div class="row justify-center">
        <p class="text-h6">
          Preencha o formulário para concessão do seu empréstimo
        </p>
      </div>
      <q-form class="col-md-7 col-xs-12 col-sm-12 q-gutter-y-md" @submit.prevent="handleSubmit">
        <q-input
          label="Nome"
          v-model="form.name"
          :rules="[val => (val && val.length > 0) || 'Name é requerido']"
        />
        <q-input
          label="CPF"
          v-model="form.cpf"
          :rules="[val => (val && val.length > 0) || 'CPF é requerido']"
        />
        <q-input
          label="Endereço"
          v-model="form.address"
          :rules="[val => (val && val.length > 0) || 'Endereço é requerido']"
        />
        <q-input
          label="Valor do Empréstimo"
          v-model="form.loan_amount"
          :rules="[val => !!val || 'Valor não pode ser vazio']"
          type="number"
          prefix="R$"
        />
        <q-btn
          label="Salvar"
          color="primary"
          class="full-width"
          rounded
          type="submit"
        />
      </q-form>
    </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'

import useNotify from 'src/composables/UseNotify'
import useApi from 'src/composables/UseApi'

export default defineComponent({
  name: 'FormPage',
  setup () {
    const form = ref({
      name: '',
      cpf: '',
      address: '',
      loan_amount: ''
    })
    const { post } = useApi()
    const { notifyError, notifySuccess } = useNotify()
    const handleSubmit = async () => {
      try {
        await post(form.value)
        notifySuccess('Saved Successfully')
      } catch (error) {
        console.log(error)
        notifyError(error.message)
      }
    }
    return {
      form,
      handleSubmit
    }
  }
})
</script>
