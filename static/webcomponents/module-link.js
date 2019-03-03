import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
      
export class ModuleLinkComponent extends LitElement {

  static get properties() {
    return {url:String};
  }
  render () {
    const {url} = this;

    return html `
    <style>
      .moduleLink {
        margin: 10px;
      }

      .moduleLink div {
        background:url('/static/modules/sketchup/FrontSlideBackdrop.png');
        padding: 10px;
        background-size: 100%;
        box-shadow: silver 5px 5px 5px;
        width:250px;
        height:150px;
      }
    </style>
    <a class="moduleLink" href="${url}">
      <div>
          <slot></slot>
      </div>
    </a>
    `;
  }
}

customElements.define('my-module-link', ModuleLinkComponent);