import { Component, OnInit } from "@angular/core";
import { ProductService } from "../../product.service";
import { Product } from "src/app/Product";

@Component({
  selector: "app-purchase-product",
  templateUrl: "./purchase-product.component.html",
  styleUrls: ["./purchase-product.component.css"],
})
export class PurchaseProductComponent implements OnInit {
  product: Product;
  errorMsg: Object;

  constructor(private productService: ProductService) {}

  ngOnInit() {}

  onSubmit(value: Product): void {
    this.productService.buyProduct(value).subscribe(
      (product: Product) => ((this.product = product), (this.errorMsg = null)),
      (error) => ((this.product = null), (this.errorMsg = error))
    );
  }
}
