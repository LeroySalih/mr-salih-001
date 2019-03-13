import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
        

export class ProComponent extends LitElement {
  render () {
    return html `<p><slot></slot></p>`
  }
}

export class ConComponent extends LitElement {
  render () {
    return html `<p><slot></slot></p>`
  }
}

export class ProsComponent extends LitElement {
  render () {
    return html `
    <style>
      .pros {
        border-right: solid 1px silver;
      }
    </style>
    <div class="pros"><slot></slot></div>`
  }
}

export class ConsComponent extends LitElement {
  render () {
    return html `
    <style>
      .cons {
        border-left: solid 1px silver;
      }
    </style>
    <div class="cons"><slot></slot></div>`
  }
}

export class ProsConsComponent extends LitElement {
  /*
  static get properties () {
    return {pros: String[],
            cons: String
    }
  }
  */
  
  render() {
    const {pros, cons} = this || {pros: [], cons: []};
    

    
    return html `
    <style>
    .pros-cons {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    </style>
    <div class="pros-cons">
      <div><h3 style="margin: 0px;">Pros</h3></div>
      <div><h3 style="margin: 0px;">Cons</h3></div>
        <slot></slot>
      </div>
    `
  }
}

customElements.define('my-pros-cons', ProsConsComponent);
customElements.define('my-pros', ProsComponent);
customElements.define('my-cons', ConsComponent);
customElements.define('my-pro', ProComponent);
customElements.define('my-con', ConComponent);