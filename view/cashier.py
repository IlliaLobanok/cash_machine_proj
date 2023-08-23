from model import *
from view import *
from command import *
from flask import Flask, render_template, request, url_for, flash, redirect, session


def index_cashier():
    if session.get("role_id") is None or session.get("role_id") != 1:
        return redirect(url_for("login"))
    return render_template("index_cashier.html", user_name="Dave")


def open_receipt():
    if session.get("role_id") is None or session.get("role_id") != 1:
        return redirect(url_for("login"))
    if session.get("current_receipt_id") is not None:
        flash("\nYou have already opened the receipt\n")
    else:
        open_command = OpenReceiptCommand(session.get("user_id"))
        receipt_id = open_command.execute_command()
        session['current_receipt_id'] = receipt_id
    return redirect(url_for('index_cashier'))


def add_product():
    if session.get("role_id") is None or session.get("role_id") != 1:
        return redirect(url_for("login"))
    product_name = request.form["product_name"]
    product_quantity = float(request.form["product_quantity"])
    add_command = AddReceiptProductCommand(session.get("current_receipt_id"), product_name, product_quantity)
    add_command.execute_command()
    return redirect(url_for('index_cashier'))


def close_receipt():
    if session.get("role_id") is None or session.get("role_id") != 1:
        return redirect(url_for("login"))
    session["current_receipt_id"] = None
    redirect(url_for('index_cashier'))
