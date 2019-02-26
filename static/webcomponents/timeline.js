import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
      
export class TimelineItemComponent extends LitElement {

  static get properties() {
    return {itemNumber: String, completed: String}
  }
  render () {
    const {itemNumber, completed} = this;

    return html `
    <style>
      .timelineItem {
        display: flex;
        flex-direction: row;
        align-items: center;
      }

      .timelineItemNumber {
        border: 2px silver solid;
        color: white;
        padding-top: 5px;
        margin: 5px;
        border-radius: 50%;
        width: 60px; 
        height: 50px;
      }

      .completed {
        background-color : green;
      }

    </style>
    <div class="timelineItem">
      <div class="timelineItemNumber ${(completed == 'true') ? 'completed' : ''}">${itemNumber}</div>
      <slot></slot>
    </div>`;
  }
}

export class TimelineComponent extends LitElement {
  static get properties () {
    return {mood: String}
  }
  
  render() {
    const {mood} = this || "OK";
    console.log(this);
    return html `
    <style>
    .timeline {
      display : grid;
      grid-template-columns: 1fr;
    }

    .timeline div {
      text-align: left !important;
      line-height: 4rem;
    }
    </style>
    <div class="timeline">
      <slot></slot>
    </div>
    `;
    
  }
}