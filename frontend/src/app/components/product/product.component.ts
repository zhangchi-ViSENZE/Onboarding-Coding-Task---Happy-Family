import { Component, Input, OnInit } from "@angular/core";
import { Product } from "src/app/Product";

@Component({
  selector: "app-product",
  templateUrl: "./product.component.html",
  styleUrls: ["./product.component.css"],
})
export class ProductComponent implements OnInit {
  // objectKeys = Object.keys; //why this can make Object.keys accessible in the template?
  // objectValues = Object.values;
  @Input() product: Product;

  constructor() {}

  ngOnInit() {}
}
