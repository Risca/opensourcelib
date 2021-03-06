/*
 * -------------------------------------------------------
 * THIS FILE IS AUTO-GENERATED!! DO NOT MODIFY DIRECTLY!!
 * THIS FILE HAS BEEN GENERATED BY THE SCRIPT:
 * seed/src/main/groovy/GenerateJobIconFile.groovy
 * VIA THE GRADLE TASK generateJobIconFiles
 * SEE GenerateJobIconFiles.groovy FOR MORE INFORMATION
 * -------------------------------------------------------
 */

package com.zenterio.jenkins

import com.zenterio.jenkins.buildtype.*
import com.zenterio.jenkins.jobtype.*

/**
 * The file name is the SHA1sum of the original image file with the file
 * extension. That is how they are identified and selected by the jenkins plugin.
 * The renaming is done by the plugin when uploaded using the upload
 * function on jenkins system management page.
 * You can also use the install script install/configure-icons to do the
 * installation of all icons at once.
 * <p>
 * Use:
<code><pre><blockquote>
install/incofigure-icons --list
</blockquote></pre></code>
 * <p>
 * to get a list of all icon files and their install names.
 */
public enum JobIcon {

    ANNOTATE("f46f3e5f3371d1268c90e1a69ef421e5a3537edf.png"),
    COMPILE("286030c8f66c2837fd671498779627cd52b123d2.png"),
    COMPILE_INC("829f50f4024f82cbf11282dc1ccadeacee8db1d7.png"),
    COVERITY("1824c323d2f7cb21d87b38d46775704c549612d3.png"),
    DCOMPILE("3a6a659a1ffd4518ac0c329c09f0fbd76f554717.png"),
    DCOMPILE_INC("6112656e3a928bf912097f97928f70d06c16bf63.png"),
    DDOCUMENTATION("ef38705ceedbb51f5b8758407aa1094d42ea246d.png"),
    DOCUMENTATION("398c71032bb9570e517f1fa81edd81fc8762a9bd.png"),
    FLASH("e2087109e7476ee9b23a38316a68f77153efeea0.png"),
    FLOW("f4843cb88da7d5ce920940bb0b11b28f8bd11bc5.png"),
    FLOW_INC("3032ec71a9c9c5c563f4d006ad0c2387589aee76.png"),
    FLOW_ORIGIN("c111396f1fd133ed199666bb89c13d6b2ffc3507.png"),
    FLOW_ORIGIN_INC("c281b1a16c9d72c1ce4026f793f5f345e17f0fe0.png"),
    FLOW_PRODUCT("3f4583faa6df0367c4775e0689895215d1cd4e85.png"),
    FLOW_PRODUCT_INC("1591cc3fa4d1947426049f0e738790231c28921d.png"),
    HELP("5be5f3fff0e6b4d185b76a2b5d27c532d625b0b0.png"),
    INC("c0c65228325d4c65167da4490251d70b7bde82b1.png"),
    PACKAGE("f504172199f05cc060a3bcdbe0fabcd49f1b3ab8.png"),
    PCOMPILE("6e2009a3deb58ced304c89b648bde08c0ebea22a.png"),
    PCOMPILE_INC("19d9d3091291b9074c4102b19c74bcdbf0fb4346.png"),
    PDOCUMENTATION("c96c09c6ee54f50feab6280aebb197f2c4b624fe.png"),
    PROMOTION("0aad897fb9265e6c8ceca2de5fc63bbc64b747e9.png"),
    RCOMPILE("cb011716b65a3f1976057f577948d9f2a031dc73.png"),
    RCOMPILE_INC("536b65101ac78b595108d4828c2d18325ee2ac77.png"),
    RDOCUMENTATION("b6f1c47b91dd67896108b15ddbadd14110a74681.png"),
    SEED("f6bd46b16cc2d28132c6e01252df5c75fd230c71.png"),
    SIGN("52e8ddba308f8182bbfc6a834d6a78fe98bebb41.png"),
    TAG("10350b94cf2fb25c24c2c32fd314b466cb98435e.png"),
    TEST_CHECKMARK("3a6f4cbf9e0649c6d26fa72c671191ef47e2192c.png"),
    TEST_DEBUG("74dd4c70dbc8a0213f0dec1a33223404e568db9e.png"),
    TEST_PRODUCT("230af68e555131e93aed61deb10d485f078a9b1b.png"),
    TEST_RELEASE("ec86d753b91a5edc3d2cc0b54414b44a1977aaa9.png"),
    UNIT_TEST("9f32625781eafc9caede00d507fe9e01d99797a1.png"),
    UNIT_TEST_INC("213c20ae9d6526450c7b342d042dfc8350a8bcac.png"),

    private String icon

    private JobIcon(String icon) {
        this.icon = icon
    }

    public String getIcon() {
        return this.icon
    }

    public String getPath() {
        return "/userContent/customIcon/${this.icon}"
    }

    public static JobIcon getCompile(BuildType buildType) {
        return COMPILE;
    }

    public static JobIcon getCompile(BuildTypeDebug debug) {
        return DCOMPILE
    }

    public static JobIcon getCompile(BuildTypeRelease release) {
        return RCOMPILE
    }

    public static JobIcon getCompile(BuildTypeProduction production) {
        return PCOMPILE
    }

    public static JobIcon getIncCompile(BuildType buildType) {
        return COMPILE_INC
    }

    public static JobIcon getIncCompile(BuildTypeDebug debug) {
        return DCOMPILE_INC
    }

    public static JobIcon getIncCompile(BuildTypeRelease release) {
        return RCOMPILE_INC
    }

    public static JobIcon getIncCompile(BuildTypeProduction production) {
        return PCOMPILE_INC
    }

    public static JobIcon getIcon(JobTypeCompile jt, BuildType bt) {
        return getCompile(bt)
    }

    public static JobIcon getIcon(JobTypeIncrementalCompile jt, BuildType bt) {
        return getIncCompile(bt)
    }

    public static JobIcon getIcon(JobTypeUnitTest jt, BuildType bt) {
        return UNIT_TEST
    }

    public static JobIcon getIcon(JobTypeIncrementalUnitTest jt, BuildType bt) {
        return UNIT_TEST_INC
    }

    public static JobIcon getIcon(JobTypeCoverity jt, BuildType bt) {
        return COVERITY
    }

    public static JobIcon getIcon(JobTypeDocumentation jt, BuildType bt) {
        return DOCUMENTATION
    }

    public static JobIcon getIcon(JobTypeFlash jt) {
        return FLASH
    }

    public static JobIcon getIcon(JobTypeSignBuild jt, BuildType bt) {
        return SIGN
    }

    public static JobIcon getIcon(JobTypeTagBuild jt) {
        return TAG
    }

    public static JobIcon getIcon(JobTypePromoteBuildChain jt) {
        return PROMOTION
    }

    public static JobIcon getIcon(JobTypeAnnotateBuildChain jt) {
        return ANNOTATE
    }

    public static JobIcon getIcon(JobTypeReleasePackaging jt) {
        return PACKAGE
    }

    public static JobIcon getIcon(JobTypeCollectArtifacts jt) {
        return PACKAGE
    }

    public static JobIcon getTestBuild(BuildTypeProduction buildType) {
        return TEST_PRODUCT
    }

    public static JobIcon getTestBuild(BuildTypeDebug debug) {
        return TEST_DEBUG
    }

    public static JobIcon getTestBuild(BuildTypeRelease release) {
        return TEST_RELEASE
    }

    public static JobIcon getIcon(JobTypeTestBuild jt, BuildType bt) {
        return getTestBuild(bt)
    }

    public static JobIcon getIcon(JobTypeIncrementalTestBuild jt, BuildType bt) {
        return getTestBuild(bt)
    }

}
