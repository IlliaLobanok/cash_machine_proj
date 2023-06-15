from model import *
from flask import Flask, render_template, request, url_for, flash, redirect, session


def index():
    return redirect(url_for("login"))


def login():
    if request.method == "POST":
        user_name = request.form["username"]
        user_password = request.form["password"]
        if not user_name or not user_password:
            flash("Username and password are required")
        else:
            found_user = MUser_DAO.read_user(user_name)
            if found_user is None:
                flash("There is no such user.")
            else:
                if hash_password(user_password) == found_user.password:
                    session["user_id"] = found_user.id
                    session["role_id"] = found_user.role_id
                    roles = MRole_DAO.read_all_roles()
                    cashier_role_id = 0
                    for role in roles:
                        if role.name == "cashier":
                            cashier_role_id = role.id
                    if found_user.role_id == cashier_role_id:
                        redirect(url_for("index_cashier"))
                else:
                    flash("The password is not correct.")

    return render_template('login.html')




