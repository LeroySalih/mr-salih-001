import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
      
export class TimelineItemComponent extends LitElement {

  static get properties() {
    return {itemNumber: String, completed: String}
  }
  render () {
    const {itemNumber, completed} = this;

    return html `
      <slot></slot>
    `;
  }
}

export class TimelineComponent extends LitElement {
  static get properties () {
    return {mood: String}
  }
  
  render() {
    const {mood} = this || "OK";
    
    return html `
    
    <slot></slot>
    
    `;
    
  }
}

customElements.define('my-timeline', TimelineComponent);
customElements.define('my-timeline-item', TimelineItemComponent);