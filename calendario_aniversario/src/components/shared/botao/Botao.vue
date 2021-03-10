<template>
  <button :class="estiloDoBotao" :type="tipo" @click="disparaAcao()">
    {{ rotulo }}
  </button>
</template>
<script>
export default {
  props: {
    tipo: {
      required: true,
      type: String,
    },

    rotulo: {
      required: true,
      type: String,
    },

    estilo: {
      required: false,
      default: "padrao",
      type: String,
    },
  },

  methods: {
    disparaAcao() {
      if (confirm("Confirma operação?")) {
        this.$emit("botaoAtivdo");
      }
    },
  },

     computed: {

       estiloDoBotao() {

           // se o valor é padrão ou não passou nada para estilo
           if(this.estilo == 'padrao') return 'botao botao-padrao';

           if(this.estilo == 'perigo') return 'botao botao-perigo';
       }
   },
};
</script>    

<style scoped>
.botao {
  display: inline-block;
  padding: 5px;
  border-radius: 5px;
  margin: 2px;
  font-size: 1.2em;
}

.botao-perigo {
  background: firebrick;
  color: white;
}

.botao-padrao {
  background: #8FA692;
  color: #F2F2F2;
}
</style>