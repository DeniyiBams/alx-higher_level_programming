#!/usr/bin/node
// class Rectangle

class Rectangle {
  constructor(w, h) {
    if (!(w <= 0 || h <= 0 || (typeof w === 'undefined' || typeof h === 'undefined'))) {
      this.width = w;
      this.height = h;
    }
  }
}
