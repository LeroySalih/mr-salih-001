import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
        
export class SlideVideoComponent extends LitElement {
  
  static get properties () {
    return { 
            videoUrl: String};
  }
  
  render() {
    const { videoUrl} = this || '';
    
    return html `
  
    <section>
      <slot name="slideTitle"></slot>
      <div class="videoDisplay">
        <div>
          <video width="80%" controls>
            <source src="${videoUrl}" type="video/mp4">
          </video>
        </div>
        <div>
          <slot></slot>
        </div>
      </div>
    </section>
    `;
  }
}


customElements.define('my-slide-video', SlideVideoComponent);