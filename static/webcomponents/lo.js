import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
        
export class LoComponent extends LitElement {
  static get properties () {
    return {mdd : String}
  }
  
  render() {
    const {mdd} = this || '';
    let mddHtml =  html`<span>Module Defintion Document not provided.</span>`;

    if (mdd != undefined) {
      mddHtml = html `
        <img src="/static/modules/PDF_file_icon.svg" style="border: none !important; margin: 0px 0px 0px 0px !important;  width:30px; height: 30px; box-shadow: none!important"> 
        <a  href="${mdd}">Link to Module Description</a>
        `; 
    } 
    return html `
    <style>
    .lo {
      text-align: left; 
      margin-bottom: 20px; 
      padding: 20px !important;
      background-color: #c7c6c6
    }

    .lo-heading {
      color: black !important;
      font-size: 1rem !important; 
    }

    .lo-question {
      color: black !important;
      text-align: left;
    }

    .lo-question ul {
      width: 100%;
    }
    </style>
    <div class="lo">
      <p class="lo-heading">LO Question:</p> 
      <p class="lo-question"><i><slot></slot></i></p>
      <div style="width: 100%; text-align: right; display: flex; flex-direction: row">
        <span>${mddHtml}</span>
      </div>
    </div>
    `
  }
}

customElements.define('my-lo', LoComponent);