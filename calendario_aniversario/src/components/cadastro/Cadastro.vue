<template>
  <div>
    <h1 v-if="foto._id" class="centralizado">Inclusão</h1>
    <h1 v-else class="centralizado">Alteração</h1>
    <h2 class="centralizado">{{ aniversario.nome }}</h2>

    <form @submit.prevent="grava()">
      <div class="controle">
        <label for="nome">Nome</label>
        <input
          v-model="aniversario.nome"
          class="field"
          id="nome"
          autocomplete="off"
        />
      </div>

      <div class="controle">
        <label for="dataAniversario">Data de aniversário</label>
        <input
          v-model="aniversario.dataAniversario"
          class="field"
          id="dataAniversario"
          type="date"
          autocomplete="off"
        />
      </div>

      <div class="centralizado">
        <meu-botao rotulo="GRAVAR" tipo="submit" :confirmacao="true" />
        <router-link to="{name: 'home'}"
          ><meu-botao rotulo="VOLTAR" tipo="button" :confirmacao="true"
        /></router-link>
      </div>
    </form>
  </div>
</template>

<script>
import Botao from "../shared/botao/Botao.vue";

import Aniversario from "../../domain/aniversario/Aniversario.js";
import AniversarioService from "../../domain/aniversario/AniversarioService.js";

export default {
  components: {
    "meu-botao": Botao,
  },

  data() {
    return {
      aniversario: new Aniversario(),
      resource: {},
      id: this.$route.params.id
    };
  },

  methods: {
    grava() {
      this.service.cadastra(this.aniversario)
      .then(() => {
        if(this.id) this.$router.push({ name: 'home' });
        this.aniversario = new Aniversario()},
        err => console.log(err));
    },
  },

    created() {

    this.service = new AniversarioService(this.$resource);

    if(this.id) {
      this.service.busca(this.id).then(aniversario => this.aniversario = aniversario);
    }
  }
};
</script>

<style scoped>
.centralizado {
  text-align: center;
}
.controle {
  font-size: 1.2em;
  margin-bottom: 20px;
}
.controle label {
  display: block;
  font-weight: bold;
}

.controle,
.controle textarea {
  width: 100%;
  font-size: inherit;
  border-radius: 5px;
}

.field {
  display: block;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
}
</style>