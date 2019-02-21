import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
        
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
      grid-template-columns: 3rem auto;
    }

    .timeline div {
      text-align: left !important;
    }
    </style>
    <h1>Timeline</h1>
    <div class="timeline">
      <div>1</div><div>What is Computer Modelling?</div>
      <div>2</div><div>Basic Concepts of SketchUp.</div>
      <div>2</div><div>How to Measure Accurately.</div>
      <div>4</div><div>How Scale, Skew, Move and Rotate.</div>
      <div>5</div><div>What are Components?</div>
      <div>6</div><div>How to build from a floor plan.</div>
      <div>7</div><div>Project - Medieval Castle.</div>
    </div>
       
    `
  }
}